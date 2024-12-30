# Telegram Bot for Dota 2 Hero Stats and Matchups

This repository contains a Python-based Telegram bot that provides Dota 2 hero statistics and matchup information. The bot interacts with users through the following commands:

1. **`/hero-stats`**: Returns basic stats for a specified Dota 2 hero.
2. **`/matchups`**: Retrieves the hero's matchups and their win rates.

## Features

- **Easy-to-use commands**: Quickly access detailed hero stats and matchup data.
- **Real-time information**: Ensures accurate and updated data using the Dota 2 API.
- **Simple deployment**: Deployable on any Python environment with Telegram Bot API support.

---

## Commands

### `/hero-stats <hero_name>`

This command provides the basic statistics for the specified Dota 2 hero.

**Example Usage:**
```
/hero-stats Pudge
```

**Response:**
```
Hero: Pudge
Attack Type: Melee
Primary Attribute: Strength
Base Health: 200
Base Mana: 50
Move Speed: 285
```

### `/matchups <hero_name>`

This command returns the hero's matchups, including win rates against other heroes.

**Example Usage:**
```
/matchups Anti-Mage
```

**Response:**
```
Matchups for Anti-Mage:
1. Hero: Meepo, Win Rate: 45%
2. Hero: Phantom Lancer, Win Rate: 47%
3. Hero: Lion, Win Rate: 53%
...
```

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/telegram-dota2-bot.git
   cd telegram-dota2-bot
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a bot on Telegram using [BotFather](https://core.telegram.org/bots#botfather) and get your bot token.

4. Set up environment variables:
   - Create a `.env` file in the project directory.
   - Add your Telegram bot token and Dota 2 API key:
     ```env
     TELEGRAM_BOT_TOKEN=your_telegram_bot_token
     DOTA2_API_KEY=your_dota2_api_key
     ```

5. Run the bot:
   ```bash
   python bot.py
   ```

---

## How It Works

1. **User Interaction**: Users send commands (`/hero-stats` or `/matchups`) to the bot on Telegram.
2. **Data Retrieval**:
   - The bot processes the command and hero name.
   - It fetches data from the Dota 2 API (or a similar data source).
3. **Response**: The bot formats the data and sends it back to the user as a message.

---

## Configuration

- **Environment Variables**: The bot uses environment variables to securely manage sensitive information such as API keys.
- **Hero Data Source**: The bot fetches hero stats and matchup data using the Dota 2 API. Ensure you have a valid API key and access permissions.

---

## Contributing

Feel free to contribute to this project! Here’s how you can help:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit: `git commit -m 'Add some feature'`
4. Push the branch: `git push origin feature-branch-name`
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Acknowledgments

- [Telegram Bot API](https://core.telegram.org/bots/api) for providing a simple interface to interact with Telegram.
- [OpenDota API](https://docs.opendota.com/) or other Dota 2 APIs for reliable hero stats and matchup data.

---

## Questions or Issues?

If you have any questions or run into any issues, feel free to open an issue on this repository or contact me on Telegram!

---
