import argparse
import taskcli.db as db
from taskcli.commands import cmd_add, cmd_list, cmd_done, cmd_del
from colorama import Fore
def build_parser():
    p = argparse.ArgumentParser(prog="taskcli")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="Ajouter")
    a.add_argument("title")
    a.add_argument("-p", "--priority", default="medium", choices=["low","medium","high"])
    a.set_defaults(func=cmd_add)
    l = sub.add_parser("list", help="Lister")
    l.add_argument("-a", "--all", action="store_true")
    l.set_defaults(func=cmd_list)
    d = sub.add_parser("done", help="Marquer faite")
    d.add_argument("id", type=int)
    d.set_defaults(func=cmd_done)
    r = sub.add_parser("del", help="Supprimer")
    r.add_argument("id", type=int)
    r.set_defaults(func=cmd_del)
    return p
def main():
    db.init_db()
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"{Fore.RED}[!] {e}")
if __name__ == "__main__":
    main()
