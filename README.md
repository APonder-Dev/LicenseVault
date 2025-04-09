# 🔐 LicenseVault

**LicenseVault** is a powerful, flexible licensing system designed for Minecraft plugin developers. Easily protect, verify, and manage your plugin licenses through a lightweight Skript-driven API with modern tools and customization features.

---

## ✨ Features

- 🔑 **License Verification** – Simple HTTP-based key checks
- 📦 **Plugin Protection** – Block access if no valid license is found
- ⚙️ **Local & Remote Storage** – Support for flatfile, YAML, and external APIs
- 💬 **Custom Kick & Deny Messages** – Styled response messages on invalid licenses
- 🧱 **Easy Integration** – Lightweight, zero-dependency Skript solution
- 🧪 **Testing Mode** – Dev-friendly bypass options

---

## 🧩 PlaceholderAPI Support

LicenseVault supports PlaceholderAPI via Skript addons like SkBee or skript-placeholders.

### Available Placeholders

| Placeholder                           | Description                       |
|--------------------------------------|-----------------------------------|
| `%licensevault_license_status%`      | Valid / Invalid / Unknown         |
| `%licensevault_license_owner%`       | License holder’s name             |
| `%licensevault_plugin_name%`         | Plugin name                       |
| `%licensevault_expiry_date%`         | License expiration date           |

---

## 📂 Project Structure

```plaintext
LicenseVault/
├── LicenseVault.sk       # Main licensing Skript
├── LICENSE               # MIT + No Resale License
└── README.md             # Documentation and usage guide
```

---

## 🛠️ Setup Instructions

1. Place `LicenseVault.sk` into `/plugins/Skript/scripts/`
2. Install any required addons (SkBee recommended)
3. Reload with `/skript reload LicenseVault`
4. Edit the script to configure license keys or verification API
5. Hook your own plugins using LicenseVault's global variables

---

## 📘 Configuration Snippet

```skript
options:
    license-check-url: "https://yourapi.com/check?key=%license%"
    kick-message: "&cInvalid license. Please purchase the plugin."
    success-log: "&aLicense validated for %player%"
```

---

## 🎯 Roadmap

- [ ] Discord License Linking
- [ ] IP Locking Support
- [ ] License Admin Panel GUI
- [ ] License Expiry Warnings
- [ ] MySQL License Caching
- [ ] Automatic Obfuscation Detection

---

## 📝 License

This project is licensed under the **MIT + No Resale** License.  
See the `LICENSE` file for full details.

---

## 💖 Donation

If you find LicenseVault useful and would like to support its development, consider making a donation. Your support helps us improve and maintain the project.

[💸 Donate on PayPal](https://www.paypal.com/donate/?business=6TUCF33LPY9K2&no_recurring=0&item_name=Development+and+Coding+Features&currency_code=USD)

---

## 📬 Contact

For any inquiries or feedback, reach out to [aponder.dev](mailto:aponder.dev)
