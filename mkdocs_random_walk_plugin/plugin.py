import os
import re
import logging

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files

from typing import Optional

import json

PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))

log = logging.getLogger('mkdocs.mkdocs_random_walk_plugin')

class RandomWalkPlugin(BasePlugin):
    config_scheme = (
        ('enabled', config_options.Type(bool, default=True)),
        ('include_paths', config_options.Type(list, default=None)),
        ('exclude_paths', config_options.Type(list, default=None)),
        ('black_list', config_options.Type(list, default=None)),
    )

    enabled = True
    is_serving = False

    def __init__(self):
        super().__init__()
        self.js_script = self._load_js_script()

    def _load_js_script(self) -> str:
        js_file_path = os.path.join(PLUGIN_DIR, 'random_walk.js')
        try:
            with open(js_file_path, 'r', encoding='utf-8') as f:
                js_content = f.read()
            return f'<script>{js_content}</script>'
        except Exception as e:
            log.error(f"Failed to load random_walk.js: {str(e)}")
            return ''

    def on_startup(self, command, **kwargs):
        self.is_serving = command == 'serve'

    def on_files(self, files: Files, config: config_options.Config) -> Optional[Files]:
        self._files = files   
        self.all_paths = []

        include_paths = self.config.get('include_paths')
        exclude_paths = self.config.get('exclude_paths')
        black_list = self.config.get('black_list')

        for file in files.documentation_pages():
            src_path = file.src_path
            
            is_exclude = False

            if include_paths:
                is_exclude = True
                for include_path in include_paths:
                    if re.match(include_path, src_path):
                        is_exclude = False
                        break

            if exclude_paths:
                for exclude_path in exclude_paths:
                    if re.match(exclude_path, src_path):
                        is_exclude = True
                        break  

            if black_list:
                for black_item in black_list:
                    if src_path.find(black_item) != -1:
                        is_exclude = True       
                        break

            if is_exclude:
                continue

            self.all_paths.append(src_path)

        return files
    

    def on_page_markdown(self, markdown: str, page: Page, **kwargs) -> str:
        if not self.enabled or not self.config.get('enabled'):
            return markdown
        
        if page.meta.get("random_walk") and self.all_paths:
            try:
                paths_json = json.dumps(self.all_paths)
                script = f'<script>window.allNotePaths = {paths_json};</script>'
                markdown += "\n" + script

                if self.js_script:
                    markdown += "\n" + self.js_script
            except Exception as e:
                log.warning(f"Random link generation failed: {str(e)}")

        return markdown

