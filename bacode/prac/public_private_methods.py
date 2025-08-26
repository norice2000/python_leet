# In Class, when creating a method use the following convention:
# Public method should have no underscore _, which signifies this is something that users can call 
# Private method have underscores _, which signifies methods to be used privately within a class

class BarcodeConfigurationParser: # think of this as the restaraunt
    def __init__(self):
        self.error_message = ['Invalid configuration']

    # public method, think of this as the waiter getting food order
    def parse(self, config_string: str):
        print("Main method which is public")

        # calling private method, think of this as the chef cooking the food roder
        config_string = self._split_configuration(config_string)
        return config_string

    # this is a private method that user not meant to know hence the _
    def _split_configuration(self, conf_string: str):
        conf_string = conf_string.split("|")
        return conf_string
    

parser = BarcodeConfigurationParser().parse("0001ABC|0002DEF")
print(parser)