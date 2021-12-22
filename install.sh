#!/usr/bin/env bash

echo -e "\e[1mThis script will install delete.py on your system, or update it if it is already installed\e[0m"
read -p "Press ENTER to start: "
echo
echo -e "\e[1mThis script will require admin priviledges to install delete.py to \e[32m/usr/local/bin\e[0m"
read -r -p $'\e[31mEnter [Y/N] to allow or prevent this: \e[0m' input
case $input in
    [yY][eE][sS]|[yY])
        curl https://raw.githubusercontent.com/Songtech-0912/Safe-Delete/master/delete.py > ~/delete
        sudo chmod a+x ~/delete
        sudo mv ~/delete /usr/local/bin
        echo -e "\e[1m\nWould you like to alias delete.py as 'rm'? This is recommended.\e[0m"
        while true
        do
            read -r -p "Your choice [Y/N]: " input
            case $input in
                [yY][eE][sS]|[yY])
                    echo "export PATH=/usr/local/bin:$PATH" >> ~/.profile
                    echo "alias rm='delete' # Added for delete.py" >> ~/.profile
                    echo "Alias created."
                    echo
                    echo -e "You can now run delete.py as \e[36mdelete\e[0m \e[32m<yourfile.txt>\e[0m"
                    echo -e "You can also run delete.py as \e[36mrm\e[0m \e[32m<yourfile.txt>\e[0m"
                    break
                    ;;
                [nN][oO]|[nN])
                    echo "Alias not created."
                    echo
                    echo -e "You can now run delete.py as \e[36mdelete\e[0m \e[32m<yourfile.txt>\e[0m"
                    break
                    ;;
                *)
                    echo "Invalid input..."
                    ;;
            esac
        done
        ;;
    [nN][oO]|[nN])
        echo Permissions were not given to script.
        echo Exiting...
        exit 1
        ;;
    *)
        echo "Invalid input..."
        exit 1
        ;;
esac

