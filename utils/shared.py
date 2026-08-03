import tomllib

class SharedContent:
    '''
    This class is a plain object, attributes of which are changed by any 
    constructor that it's passed to. Its purpose is to store other 
    module/class/object instance references for use by other 
    module/class/object instances.
    '''
    def __init__(self):
        pass

    def load_config(self, path):
        '''
        Loads and stores the config by a given file path. 
        '''
        with open(path, 'rb') as f:
            self.config = tomllib.load(f)
            print(f"Loaded config: {self.config['Version']['config']}")