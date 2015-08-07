#!/usr/bin/env python

from optparse import OptionParser
from user_analyze import user_analyze

EXT_ERR = 1

class options_parse:
    def __init__(self):
        options = self.options()
        api = "https://api.vk.com/method/"
        self.verify_options(options)
        c1 = user_analyze()
        user_data = c1.get_user_id(api=api, user_id=options["id"])
        users_friends = c1.get_user_friends(api=api, user_id=user_data[0])
        print "Personal data: {0} \nFriends: {1}".format(user_data, users_friends)

    def options(self):
        parser = OptionParser()
        parser.add_option("-a", "--analyze", dest="analyze",
                          type="string",
                          help="Type of data which is needed to analyze")
        parser.add_option("-i", "--id", dest="id",
                          type="string", help="User\'s or group identificator")
        options = vars(parser.parse_args()[0])
        return options

    def verify_options(self, options):
        if options["analyze"] == "user":
            pass
        elif options["analyze"] == "group":
            pass
        elif not options["analyze"]:
            print "Option --analyze is empty"
            exit(EXT_ERR)
        else:
            print "Unexpected data {0} in option --analyze".format(options["analyze"])
            exit(EXT_ERR)
        return options


if __name__ == "__main__":
    data = options_parse()
