


        for param in args_list[1:]:
            key, value = param.split('=')

            """This checks if the value starts and ends with double quotes"""
            if value.startswith('"') and value.endswith('"'):
                """ To Remove the quotes and replace underscores with spaces"""
                value = value[1:-1].replace('_', ' ')
            elif '.' in value:
                """Check if value is a float"""
                try:
                    value = float(value)
                except ValueError:
                    print(f"Invalid value for {key}: {value}")
                    return
            elif value.isdigit():
                """Check if value is a int"""
                value = int(value)

            """Adds key-value pair to dict"""
            params[key] = value

        """Creates a new instance """
        new_inst = HBNBCommand.classes[class_name](**params)

        # Save the new instance
        storage.save()

        print(new_inst.id)
        storage.save()
