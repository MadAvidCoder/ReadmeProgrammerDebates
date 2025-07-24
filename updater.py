import pathlib
import re
import random

def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '\n{}\n'.format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)

questions = ['Is Vibe Coding good?', "Are spaces or tabs better?", "Dark mode or Light mode?", "Is Vim or Emacs better?", "Frontends or Backends?", "Is Git Rebase or Git Merge better?", "Should we use Inline CSS or External Stylesheets?", "Should tabs be 2 spaces or 4 spaces?", "CSS: Flexbox or grid?", "YAML or JSON? Which is better?"]
answers = [['Yes', 'No'], ["Spaces", "Tabs"], ["Dark Mode", "Light Mode"], ["Vim", "Emacs"], ["Frontend", "Backend"], ["Git Rebase", "Git Merge"], ["Inline CSS", "External Stylesheets"], ["2 Spaces", "4 Spaces"], ["Flexbox", "Grid"], ["YAML", "JSON"]]

def pick_random_question():
    global questions
    question = random.choice(questions)
    options = answers[questions.index(question)]
    return question, options

def make_shield(label, endpoint):
    return '![Results {}](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fmadavidcoder.hackclub.app%2Fresults-{}&query=%24.value&label={})'.format(endpoint, endpoint, label)

root_path = pathlib.Path(__file__).parent.resolve()

readme_path = root_path / '../README.md'

readme = readme_path.open().read()
q, a = pick_random_question()
added_questions = replace_chunk(readme, 'Question', q, inline=True)
readme_path.open('w').write(added_questions)

readme = readme_path.open().read()
add_opt_1 = replace_chunk(readme, 'Option 1', a[0], inline=True)
readme_path.open('w').write(add_opt_1)

readme = readme_path.open().read()
add_opt_2 = replace_chunk(readme, 'Option 2', a[1], inline=True)
readme_path.open('w').write(add_opt_2)

readme = readme_path.open().read()
add_results_1 = replace_chunk(readme, 'Results 1', make_shield(a[0], '1'), inline=True)
readme_path.open('w').write(add_results_1)

readme = readme_path.open().read()
add_results_2 = replace_chunk(readme, 'Results 2', make_shield(a[1], '2'), inline=True)
readme_path.open('w').write(add_results_2)