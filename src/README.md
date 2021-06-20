# Backend Design Document

## Overview
- `settings.py`: store continuously updated settings config data for user, session, portal, theater for both rest mode and collaborative/social mode
- `api.py`: assume we need to write more functions to get particular data / storing in memcache/store specific to Oculus App, and general api connections and endpoints; define API-specific objects specific to Oculus App, Unity Unreal Game Engine
- `client.py `: API client
