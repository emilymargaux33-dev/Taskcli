import argparse
from colorama import Fore, Style, init
from . import db

init(autoreset=True)

def cmd_add(args):
    tid = db.add_task(args.title)
    print(f"{Fore.GREEN}[+] Tâche #{tid} ajoutée : {args.title}")

def cmd_list(args):
    rows = db.list_tasks(show_done=args.all)
    if not rows:
        print(f"{Fore.YELLOW}Aucune tâche.")
        return
    for r in rows:
        status = f"{Fore.GREEN}✓" if r["done"] else f"{Fore.YELLOW}○"
        print(f"{status} [{r['id']}] {r['title']}  {Style.DIM}({r['created_at']})")

def cmd_done(args):
    n = db.complete_task(args.id)
    if n:
        print(f"{Fore.GREEN}[+] Tâche #{args.id} terminée.")
    else:
        print(f"{Fore.RED}[!] Introuvable.")

def cmd_del(args):
    n = db.delete_task(args.id)
    if n:
        print(f"{Fore.GREEN}[+] Tâche #{args.id} supprimée.")
    else:
        print(f"{Fore.RED}[!] Introuvable.")

def build_parser():
    p = argparse.ArgumentParser(prog="taskcli", description="Gestionnaire de tâches CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="Ajouter une tâche")
    a.add_argument("title")
    a.set_defaults(func=cmd_add)

    l = sub.add_parser("list", help="Lister les tâches")
    l.add_argument("-a", "--all", action="store_true", help="Inclure les terminées")
    l.set_defaults(func=cmd_list)

    d = sub.add_parser("done", help="Marquer comme terminée")
    d.add_argument("id", type=int)
    d.set_defaults(func=cmd_done)

    r = sub.add_parser("del", help="Supprimer une tâche")
    r.add_argument("id", type=int)
    r.set_defaults(func=cmd_del)

    return p

def main():
    db.init_db()
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
