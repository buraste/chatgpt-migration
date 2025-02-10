# ChatGPT Conversation Migration Tool

**Easily split and export large ChatGPT conversation data into separate JSON files to help move your old chats into a new ChatGPT account.**

## Overview

OpenAI currently does **not** allow changing your account email nor importing conversation data into a new account.

However, you _can_ export your entire conversation history (including images, audio links, and text) as a JSON file from your old account by going to:

```

Settings > Data controls > Export Data

```

Once the export is done, OpenAI emails you a ZIP file containing a `conversations.json` file. **The `migration.py` script** will take this file, split each conversation out into its own JSON file in chronological order, and place them in a folder called `conversations`.

---

## Why You Need It

1.  **Moving Chats**: If you start a **new** ChatGPT account, there’s no official “import” feature yet.

2.  **Organization**: This tool splits your large `conversations.json` into manageable individual JSON chat files—perfect for archiving or referencing.

3.  **Manual Re-import**: With these smaller JSON files, you can open a new chat in your new ChatGPT account and paste or “upload” the conversation piece by piece, prompting ChatGPT to “learn” your old context.

---

## Installation

1.  **Clone or Download** this repository.

2.  Make sure you have **Python 3.9 or newer** installed on your system.

3.  Place the `migration.py` script in a folder of your choice.

---

## Usage

1.  **Export** your data from your old ChatGPT account via the official “Export Data” functionality.

2.  **Unzip** the file OpenAI sends, and locate the `conversations.json` inside.

3.  **Copy** this `conversations.json` into the **same directory** as `migration.py`

&mdash; **OR** keep it anywhere and simply provide its file path in the command line.

### Running the Script

- **Option 1**: If your file is literally named `conversations.json` and located next to `migration.py`, just run:

```bash

python migration.py

```

- **Option 2**: If your file is in a different location or has a different name, specify it as an argument:

```bash

python migration.py /path/to/your/conversations.json

```

After running this script, you’ll see a new folder named `conversations` in the same directory as `migration.py`. Inside, you’ll find individual `.json` files named with the following format:

```

1_Some_Conversation_Title_01.01.2025.json

2_Another_Conversation_Title_02.01.2025.json

...

```

> The script sorts conversations by **reverse** chronological order (most recent first), using `update_time` (if available) or `create_time` as a fallback.

---

## Importing to Your New ChatGPT Account

Currently, OpenAI provides **no official import** feature. However, you can work around this by:

1. Opening a **new chat** in your new ChatGPT account (on [chat.openai.com](https://chat.openai.com) or the ChatGPT desktop app).

2. **Drag and drop** one of the split JSON files (e.g., `1_Some_Conversation_Title_01.01.2025.json`) directly into the chat window with a prompt like:

```

I am giving you a conversation we had in the past as JSON.

Please learn the whole thing. Here it is:

```

3.  **Send** that message to ChatGPT.

4.  **Optionally**, rename the new chat’s title to match the original conversation (e.g., “Some Conversation Title”).

5.  **Repeat** for each conversation you want to bring over.

Yes, it’s a bit tedious. But it’s currently the only known method to “import” them.

**Happy migrating!**

## Contributing

1.  **Fork** the repository.

2.  **Create** a new branch (`bash git checkout -b feature/new-feature `).

3.  **Commit** your changes (`bash git commit -m 'Add some new feature' `).

4.  **Push** to the branch (`bash git push origin feature/new-feature `).

5.  **Open a Pull Request** explaining your changes.

## FAQs

**1. How can I change my ChatGPT email address?**  
Currently, OpenAI does not provide a way to directly change the email address associated with your ChatGPT account. If you need to use a different email, you’ll have to create a new account.

**2. Can I change my email address on ChatGPT?**  
No. At this time, there is no built-in feature on ChatGPT or OpenAI’s platform to switch your email address.

**3. Is it possible to change my ChatGPT email address?**  
It’s not possible through any official means. You would need to export your data (if necessary) and open a new account under the email address you want to use.

**4. Can you change your OpenAI account email?**  
No, OpenAI does not currently support any form of email change for an existing account.

**5. Can I change my ChatGPT email address without creating a new account?**  
Unfortunately, no. You must create a new account with your desired email address if you wish to switch.

## License

This project is open source and can be used, modified, and distributed by **anyone**. You are free to **copy**, **edit**, and **share** it as needed. For detailed terms, see the [LICENSE](LICENSE) file (MIT License).

---