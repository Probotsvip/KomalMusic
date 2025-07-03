# Komal Music Bot - Architecture Overview

## Overview

This is a Telegram music bot built using Python, Pyrogram, and PyTgCalls. The bot allows users to play music and videos in Telegram voice/video chats, supporting multiple platforms including YouTube, Spotify, SoundCloud, and local files. The system is designed with a modular architecture, featuring separate components for bot management, music streaming, user interaction, and administrative functions.

## System Architecture

### Core Technologies
- **Framework**: Pyrogram (Telegram Bot API wrapper)
- **Audio/Video Streaming**: PyTgCalls
- **Database**: MongoDB (using Motor async client)
- **Media Processing**: FFmpeg, yt-dlp
- **Language**: Python 3.x

### Application Structure
The application follows a modular architecture with clear separation of concerns:

```
KomalMusic/
â”œâ”€â”€ core/           # Core functionality (bot, userbot, call handling)
â”œâ”€â”€ platforms/      # Media platform integrations
â”œâ”€â”€ plugins/        # Feature modules (admins, play, sudo, tools)
â”œâ”€â”€ utils/          # Utility functions and helpers
â””â”€â”€ misc.py         # Global variables and configurations
```

## Key Components

### 1. Bot Core (`KomalMusic/core/`)
- **Bot Client**: Main Telegram bot instance handling user interactions
- **Userbot Client**: Assistant account for joining voice chats
- **Call Handler**: PyTgCalls integration for audio/video streaming
- **Directory Management**: File system organization

### 2. Platform Integrations (`KomalMusic/platforms/`)
- **YouTube API**: Primary music source with search and streaming
- **Spotify API**: Playlist and track metadata (requires credentials)
- **SoundCloud API**: Alternative music platform support
- **Apple Music API**: Basic support framework
- **Local Files**: Direct file playback support
- **Telegram**: Media download from Telegram messages

### 3. Plugin System (`KomalMusic/plugins/`)
- **Admin Commands**: Voice chat control (pause, resume, skip, etc.)
- **Play Commands**: Music/video playback functionality
- **Sudo Commands**: Super admin features (maintenance, broadcasting)
- **Tools**: Utility commands (ping, stats, lyrics, etc.)

### 4. Database Layer (`KomalMusic/utils/database.py`)
- **User Management**: Served users, blocked users, sudo users
- **Chat Management**: Served chats, blacklisted chats
- **Settings**: Language preferences, play modes, video limits
- **Authorization**: Admin authentication system

## Data Flow

### Music Playback Flow
1. User sends play command with query/URL
2. System validates permissions and chat status
3. Platform-specific API extracts media information
4. Media is queued or streamed directly via PyTgCalls
5. Playback status is stored in memory (db dict)
6. Real-time updates sent to users

### Command Processing Flow
1. Pyrogram filters route commands to appropriate handlers
2. Decorators apply language localization and permission checks
3. Database operations update persistent state
4. Response sent with appropriate markup/formatting

### Administrative Flow
1. Admin commands require specific permissions
2. Chat admin cache maintained for performance
3. Actions logged and can be broadcasted
4. Settings changes affect bot behavior globally or per-chat

## External Dependencies

### Required Services
- **MongoDB**: Primary database for persistent storage
- **Telegram Bot API**: Core bot functionality
- **Telegram MTProto API**: Userbot operations

### Optional Services
- **Spotify API**: Enhanced music discovery (CLIENT_ID/SECRET required)
- **Heroku**: Deployment platform support
- **Various Media APIs**: YouTube, SoundCloud integration

### System Dependencies
- **FFmpeg**: Audio/video processing and conversion
- **Python Packages**: Pyrogram, PyTgCalls, Motor, yt-dlp, and others

## Deployment Strategy

### Environment Configuration
The application uses environment variables for configuration:
- Bot credentials (BOT_TOKEN, API_ID, API_HASH)
- Database connection (MONGO_DB_URI)
- Optional service integrations (SPOTIFY_CLIENT_ID, etc.)
- Feature toggles (AUTO_LEAVING_ASSISTANT, etc.)

### Deployment Options
- **Local Deployment**: Direct Python execution with setup.py
- **Heroku**: Cloud deployment with Heroku-specific configurations
- **VPS/Server**: Manual deployment with system dependencies

### Initialization Process
1. Install system dependencies (FFmpeg, Python packages)
2. Create necessary directories (downloads, cache, logs)
3. Load environment configuration
4. Initialize database connections
5. Start bot and userbot clients
6. Load plugin modules dynamically
7. Begin auto-leave and cleanup tasks

## Recent Changes

- **July 03, 2025**: Successfully deployed Telegram Music Bot
  - Installed all required dependencies (Pyrogram, PyTgCalls, motor, etc.)
  - Configured FFmpeg for audio processing
  - Set up MongoDB database integration with user-provided credentials
  - Fixed PyTgCalls compatibility issues for modern library versions
  - Created simplified call handler for voice chat functionality
  - Added missing database functions for active chats and music status
  - Loaded all 38 plugin modules successfully
  - Bot is now running and ready for use with full music streaming capabilities

## Changelog

- July 03, 2025. Initial setup and successful deployment

## User Preferences

Preferred communication style: Simple, everyday language.
