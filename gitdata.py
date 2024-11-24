import requests
import os
import json
from xml.etree import ElementTree as ET
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Function to update variables based on parsed data


def update_variables_from_svg(svg_content):
    variables = {
        "OS": None,
        "Uptime": None,
        "Host": None,
        "Kernel": None,
        "IDE": None,
        "Programming Languages": None,
        "Computer Languages": None,
        "Real Languages": None,
        "Hobbies Software": None,
        "Hobbies Hardware": None,
        "Email": None,
        "LinkedIn": None,
        "Discord": None,
        "Repos": None,
        "Commits": None,
        "Stars": None,
        "Followers": None,
        "Lines of Code": None,
    }

    # Parse SVG content
    root = ET.fromstring(svg_content)
    texts = root.findall(".//{http://www.w3.org/2000/svg}text")

    # Extract key-value pairs
    for text in texts:
        lines = text.findall("{http://www.w3.org/2000/svg}tspan")
        for line in lines:
            if line.text:
                parts = line.text.split(":")
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()
                    if key in variables:
                        variables[key] = value

    return variables, root


# Function to update the SVG content with new variables
def write_updates_to_svg(svg_root, updates):
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    texts = svg_root.findall(".//svg:text", namespaces)

    for text in texts:
        lines = list(text)  # Get all child <tspan> elements
        for i in range(len(lines) - 1):
            key_tspan = lines[i]
            value_tspan = lines[i + 1]

            if key_tspan.tag == f"{{{namespaces['svg']}}}tspan" and value_tspan.tag == f"{{{namespaces['svg']}}}tspan":
                key = key_tspan.text.strip() if key_tspan.text else None

                if key in updates and updates[key] is not None:
                    # Update the value in the corresponding sibling <tspan>
                    value_tspan.text = updates[key]

    return svg_root


# SVG Content (input from user)
svg_content = """<?xml version="1.0" encoding="utf-8"?><svg xmlns="http://www.w3.org/2000/svg" font-family="Andale Mono,AndaleMono,Consolas,monospace" width="1105px" height="550px" font-size="16px">
<style>
.keyColor {fill: #953800;}
.valueColor {fill: #0a3069;}
.addColor {fill: #1a7f37;}
.delColor {fill: #cf222e;}
.commentColor {fill: #8b949e;}
text, tspan {white-space: pre;}
</style>

<rect width="1100px" height="530px" fill="#f6f8fa" rx="15"/>

<text x="15" y="30" fill="#24292f" class="ascii">
<tspan x="15" y="30">                ..-+#@@@@@@%*+-..                   </tspan>
<tspan x="15" y="50">              ..=%@@@@@@@@@@@@@#-..                 </tspan>
<tspan x="15" y="70">             .-#@@@@@@@@@@@@@@@@@*:.                </tspan>
<tspan x="15" y="90">            .=%@@@@@@%%%##*****#%%*..               </tspan>
<tspan x="15" y="110">            -%@@@#**+++=========+#%=.              </tspan>
<tspan x="15" y="130">            .*@@@#*+++++==========+%*.             </tspan>
<tspan x="15" y="150">            .#@@@#++++++===========%=.             </tspan>
<tspan x="15" y="170">           ..#@@#+*#*****++=++**+++*:.             </tspan>
<tspan x="15" y="190">           .=*%%*+**##%##*+++*##*+=+*:             </tspan>
<tspan x="15" y="210">           .+**#+++++*****+++++++===+-             </tspan>
<tspan x="15" y="230">           .-+***+++++++**+++++======:             </tspan>
<tspan x="15" y="250">            .:=*****+++****+++++====-.             </tspan>
<tspan x="15" y="270">              .+**************+++++-               </tspan>
<tspan x="15" y="290">               -*************+**+++:               </tspan>
<tspan x="15" y="310">               .*##****++***++++++-.               </tspan>
<tspan x="15" y="330">               .=#####****++++***-.                </tspan>
<tspan x="15" y="350">              .:=*##%%##********:.                 </tspan>
<tspan x="15" y="370">            .-%*==+**#######**+=..                 </tspan>
<tspan x="15" y="390">         ..:*@@%+===++**+++++++-=:..               </tspan>
<tspan x="15" y="410">      ..:+#@@@@@#====--=++++++--*@%*=-..           </tspan>
<tspan x="15" y="430">   ...=#@@@@@@@@@#+==----+*#*++=+@@@@@@#+-....     </tspan>
<tspan x="15" y="450"> .-+#@@@@@@@@@@@@@#+==+*####****+@@@@@@@@@@%#+-..  </tspan>
<tspan x="15" y="470"> %@@@@@@@@@@@@@@@@@*+=++*####*+=-+@@@@@@@@@@@@@+.  </tspan>
<tspan x="15" y="490"> %@@@@@@@@@@@@@@@@@%*++++*#%#*+=-=#@@@@@@@@@@@@@-. </tspan>
<tspan x="15" y="510"> +******************=---===++==-::-*************-. </tspan>
</text>

<text x="470" y="30" fill="#24292f">
<tspan x="470" y="30">stephen@bannister</tspan>
<tspan x="470" y="50">——————</tspan>
<tspan x="470" y="70" class="keyColor">OS</tspan>: <tspan class="valueColor">Windows 11, iOS</tspan>
<tspan x="470" y="90" class="keyColor">Uptime</tspan>: <tspan class="valueColor">TBC</tspan>
<tspan x="470" y="110" class="keyColor">Host</tspan>: <tspan class="valueColor">Sheffield Hallam University</tspan>
<tspan x="470" y="130" class="keyColor">Kernel</tspan>: <tspan class="valueColor">MSc Computer Science with Artificial Intelligence</tspan>
<tspan x="470" y="150" class="keyColor">IDE</tspan>: <tspan class="valueColor">VSCode 1.95.2</tspan>
<tspan x="470" y="190" class="keyColor">Languages</tspan>.<tspan class="keyColor">Programming</tspan>: <tspan class="valueColor">Python</tspan>
<tspan x="470" y="210" class="keyColor">Languages</tspan>.<tspan class="keyColor">Computer</tspan>: <tspan class="valueColor">HTML, CSS</tspan>
<tspan x="470" y="230" class="keyColor">Languages</tspan>.<tspan class="keyColor">Real</tspan>: <tspan class="valueColor">English</tspan>
<tspan x="470" y="270" class="keyColor">Hobbies</tspan>.<tspan class="keyColor">Software</tspan>: <tspan class="valueColor">Neural Networks, Social Media Tools</tspan>
<tspan x="470" y="290" class="keyColor">Hobbies</tspan>.<tspan class="keyColor">Hardware</tspan>: <tspan class="valueColor">Raspberry Pi Builds, High Performance PC Builds</tspan>
<tspan x="470" y="330" class="keyColor">Contact</tspan>:
<tspan x="470" y="350">——————</tspan>
<tspan x="470" y="370" class="keyColor">Email</tspan>: <tspan class="valueColor">stephen@piroma.co.uk</tspan>
<tspan x="470" y="390" class="keyColor">LinkedIn</tspan>: <tspan class="valueColor">smbannister</tspan>
<tspan x="470" y="410" class="keyColor">Discord</tspan>: <tspan class="valueColor">nope</tspan>
<tspan x="470" y="450" class="keyColor">GitHub Stats</tspan>:
<tspan x="470" y="470">——————</tspan>
<tspan x="470" y="490" class="keyColor">Repos</tspan>: <tspan class="valueColor">TBC</tspan> {<tspan class="keyColor">Contributed</tspan>: <tspan class="valueColor">TBC</tspan>} | <tspan class="keyColor">Commits</tspan>: <tspan class="valueColor">TBC  </tspan> | <tspan class="keyColor">Stars</tspan>: <tspan class="valueColor">TBC</tspan>
<tspan x="470" y="510" class="keyColor">Followers</tspan>: <tspan class="valueColor">TBC </tspan> | <tspan class="keyColor">Lines of Code</tspan>: <tspan class="valueColor">TBC</tspan> (<tspan class="addColor">TBC++</tspan>, <tspan class="delColor">TBC--</tspan>)
</text>

</svg>"""

# ----------------- Data Update Functions --------------------


def date_difference(prior_date_str="1976-08", date_format="%Y-%m"):
    ''' Calculate the difference between today's date and a given prior date.

    Args:
        prior_date_str (str): The prior date as a string (e.g., "2020-05").
        date_format (str): The format of the input prior date (default is "%Y-%m").

    Returns:
        tuple: A tuple containing the difference in years and months.
    '''

    # Parse the prior date
    prior_date = datetime.strptime(prior_date_str, date_format)
    # Get today's date
    today = datetime.today()
    # Calculate the difference
    diff = relativedelta(today, prior_date)
    # Return the differences
    return diff.years, diff.months


def get_vscode_version_windows():
    try:
        # Default VSCode installation path (adjust if needed)
        vscode_path = os.path.expandvars(r"%HOMEPATH%\AppData\Local\Programs\Microsoft VS Code\resources\app\package.json")
        if not os.path.exists(vscode_path):
            return "VSCode installation not found at the default location."

        # Read the package.json file to extract version
        with open(vscode_path, 'r', encoding='utf-8') as f:
            package_data = json.load(f)
            return package_data.get("version", "Version info not found in package.json.")
    except Exception as e:
        return f"An error occurred: {e}"


def get_github_metrics(username="StephenBannister", token=None):
    """
    Fetch various GitHub metrics for a given user.

    Args:
        username (str): GitHub username.
        token (str): GitHub personal access token (optional, for authenticated requests).

    Returns:
        dict: Dictionary containing metrics like repos, commits, stars, followers, lines of code, etc.
    """
    base_url = f"https://api.github.com/users/{username}"
    headers = {'Authorization': f'token {token}'} if token else {}

    try:
        # Fetch user details (followers and public repos)
        user_response = requests.get(base_url, headers=headers)
        if user_response.status_code != 200:
            return {"error": f"Failed to fetch user details: {user_response.json().get('message')}"}
        user_data = user_response.json()

        # Followers
        followers = user_data.get("followers", 0)

        # Fetch all repositories
        repos_url = user_data.get("repos_url", f"{base_url}/repos")
        repos = []
        while repos_url:
            repo_response = requests.get(repos_url, headers=headers)
            if repo_response.status_code != 200:
                return {"error": f"Failed to fetch repositories: {repo_response.json().get('message')}"}
            repos.extend(repo_response.json())
            repos_url = repo_response.links.get(
                'next', {}).get('url')  # Handle pagination

        # Calculate metrics
        public_repos = len(repos)
        stars = sum(repo.get("stargazers_count", 0) for repo in repos)
        contributed_repos = len(
            [repo for repo in repos if repo.get("fork")])  # Forked repos
        lines_of_code = 0

        # Commits count (requires authenticated requests)
        commits = 0
        for repo in repos:
            commits_url = repo.get("commits_url", "").replace("{/sha}", "")
            commits_response = requests.get(commits_url, headers=headers)
            if commits_response.status_code == 200:
                commits += len(commits_response.json())
            # Optionally, add detailed commit counting here (if needed)

        # Prepare the result
        metrics = {
            "followers": followers,
            "public_repos": public_repos,
            "contributed_repos": contributed_repos,
            "stars": stars,
            "commits": commits,
            # Placeholder (difficult to calculate via API alone)
            "lines_of_code": lines_of_code,
        }

        return metrics

    except Exception as e:
        return {"error": f"An error occurred: {e}"}




def update_values():
    # Process the data gathering functions
    years, months = date_difference()
    vsc_version = get_vscode_version_windows()
    gh_metrics = get_github_metrics()

    # Update the data dictionary ready to write to SVG file
    updates["IDE"] = "VSCode 1.95.2"
    updates["Uptime"] = f"{years} years, {months} months"
    updates["IDE"] = f"VS Code version {vsc_version}"
    updates["Repos"] = f"{gh_metrics['public_repos']}"
    updates["Contributed"] = f"{gh_metrics['contributed_repos']}"
    updates["Commits"] = f"{gh_metrics['commits']}"
    updates["Stars"] = f"{gh_metrics['stars']}"
    updates["Followers"] = f"{gh_metrics['followers']}"
    updates["Lines of Code"] = f"{gh_metrics['lines_of_code']}"


if __name__ == "__main__":

    # Step 1: Extract variables and SVG root
    variables, svg_root = update_variables_from_svg(svg_content)

    # Step 2: Update some variables (example updates)
    updates = {
        "OS": "Windows 11 Pro, iOS",
        "Uptime": None,
        "Email": "stephen@piroma.co.uk",
        "Host": None,
        "Kernel": None,
        "IDE": None,
        "Programming Languages": None,
        "Computer Languages": None,
        "Real Languages": None,
        "Hobbies Software": None,
        "Hobbies Hardware": None,
        "LinkedIn": None,
        "Discord": None,
        "Repos": None,
        "Contributed": None,
        "Commits": None,
        "Stars": None,
        "Followers": None,
        "Lines of Code": None,
    }


    # Step 3: Update all the dynamic values for use in the SVG content
    update_values()

    # Step 4: Write updates to SVG content
    updated_svg_root = write_updates_to_svg(svg_root, updates)

    # Step 5: Write the updated SVG content to a file
    updated_svg_content = ET.tostring(updated_svg_root, encoding="unicode")
    with open("light_mode.svg", "w", encoding="utf-8") as file:
        file.write(updated_svg_content)

    print("SVG updated and saved as 'light_mode.svg'.")
