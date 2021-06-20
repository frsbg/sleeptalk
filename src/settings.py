



class RestModeSettingsConfig:
    # settings in Rest Mode
    # SettingsConfig handles settings defined in Menu
        # prompt first time to configure; later pull up the menu bar
    def __init__(self):
        self.brightness_value = 0
        self.lock_movement : bool = False
        # default = 100
        self.character_populate : bool = False
        self.weather : Tuple = ["rain", "thunderstorm", "snow", "clear"]
        # brown noise; environment objects
        environment_settings = {
            "animals": False,
            "distinct_weather" : False
            
        }
        # environment settings defined is no t existent
        environment_settings_on : bool = False
        # preset sounds
        self.add_brown_noise_state : bool = False
        self.add_white_noise_state : bool = False
        # playlist object with oculus --> search query as function of oculus-native api endpoint for music
        self.brightness_config= self.configure_brightness_value()
        self.user_geolocation : Tuple = (self.client_lattitude, self.client_longitude)
        self.client_lattitude = self.get_client_lattitude()
        self.client_longitude = self.get_client_longitude()
        self.user_receives_prompt : bool = self.get_user_prompt_state()
        self.user_rest_mode_session_state : bool = self.get_session_state()
        # set of defined scenes like nighttime, morning, sunset, woods, ocean/beach, etc
        # we store the state of the user's inputs as well as calculate our own states to track internally
        self.user_scene_selection = self.get_user_scene_selection()
        self.scenes : Map = []

    def get_user_scene_selection():
        return ""

    def get_client_lattitude():
        return []

    def get_client_longitude():
        return []

    def get_user_prompt_state():
        return []


    def configure_brightness_value():
        # schedule is prefixed akin to f.lux
        # we need oculus endpoint to read in the input of the user (read in user response when they update menu on first and nth response)
        brightness_value_default = 2500
        # endpoints remove need for parameters
        self.brightness_value = brightness_value_default

    def get_session_state():
        # use api to check for if the session has been closed
        self.user_rest_mode_session_state = False

    def get_scene_config():
        return ""

class Map(object):
    def __init__(self):
        # we need to get the actual Oculus/Unity Game Engine object for preset scenes
        # scene metadata
        # pull virtual world samples as scenes to use
        

class MultiplayerBrowserSettingsConfig():
    def __init__(self):
        # app will ask what the dominant hand is and then we will read a set of available triggers; left and right
        self.dominant_hand : str = self.get_user_dominant_hand()
        # the 4 settings that dominant hand changes will be written here below, where dominant hand str is passed continuously
        self.pointer_trigger = self.get_pointer_trigger(self.dominant_hand)
        self.middle_trigger = self.get_middle_trigger()
        self.left_trigger = self.get_left_trigger()
        self.clients : Tuple[Client] = []
        

    def get_user_dominant_hand():
        # read in the input when giving a set of questions to define/configure settings (intro)
        return ""
    

class Client:
    def __init__(self):
        # user information
        self.client_name = self.get_client_name()
        self.client_id = self.get_client_id()
        # register user behavior and actions in environment
        self.client_state : bool = False
        self.client_wants_to_logout : bool = False
        self.client_scroll_sensitivity : float = 0
        # multiplier
        self.client_movement_speed : int = 1 #(0,1)


    def get_client_name():
        return ""

    def get_client_id() -> str:
        return ""

class Session:
    # define schema of Session object
    def __init__(self):
        # since void params, we need to track the state of the memcache or list of friends to add based on click actions; or find a simpler approach with their browser API 
        # read in user to kick based on quick menu data, then remove user from session
        self.session_time = self.get_session_time() # options : Tuple
        

    def invite_players(owner_id, port):
        return None
    
    def logout():
        if (self.client_state == False):
            # use oculus after given prompt from user to exit app
            return ""

        if (self.client_state == True):
            return ""

    def check_to_logout():
        if (self.client_wants_to_logout):
            self.logout()

        else if (self.client_wants_to_logout == False);
            return None
    
    def make_screen_private():
        # if data is sensitive, then hide screen
        return None

    def create_session():
        return None

    def lock_session():
        return None
    
    def friendUser():
        return None

    def block_user():
        return None

    def transferOwnership():
        return None

    def direct_message_user():
        return None

    def close_session():
        # onSessionClosed()
        # session closed and users go back to main screen or lobby (ask for user e.g. two options)
        return None
    
    def read_client_keyboard_data():
        return None

    def kick_client():
        # check permissions for owner/admin
        return None

    def get_subscription_auth():
        # check for netflix/youtube subscriptions/login information for watch party
        return None

    def mute_player():
        # client can access their quick menu to mute player
        return None

    def get_search_bar():
        return None

    def pull_up_search_bar():
        search_bar = self.get_search_bar()
        return None

    def create_quick_menu():
        # DM is important
        self.quick_menu : Tuple = [self.kickUserOption, self.blockUserOption, self.transferOwnership, self.friendUser, self.direct_message_user]


if __name__ == '__main__':
    # todo: create an object to track the state of the existing object to change the object's data or the config/settings data
    # termination_state depends on the user's logged state in the Oculus App (we need endpoint)
    termination_state : bool = False
    while not termination_state:
        # create settings config object continuously to store state
        settings_config = SettingsConfig()
        if (termination_state == True):
            termination_state = True

     

