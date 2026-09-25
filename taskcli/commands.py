import taskcli.db as db
from colorama import Fore, Style
def cmd_add(args):
    db.add_task(args.title, args.priority)
    print(f"{Fore.GREEN}✓ Ajouté: {args.title} [{args.priority}]{Style.RESET_ALL}")
def cmd_list(args):
    rows = db.list_tasks(args.all)
    if not rows:
        print("Aucune tache")
        return
    for i, t, d, p in rows:
        s = "✓" if d else "○"
        c = Fore.GREEN if d else Fore.YELLOW
        pr = f"{Fore.RED}[HIGH]" if p=="high" else f"{Fore.BLUE}[LOW]" if p=="low" else "[MED]"
        print(f"{c}{i}. {s} {t} {pr}{Style.RESET_ALL}")
def cmd_done(args):
    conn = db.get_conn()
    conn.execute("UPDATE tasks SET done=1 WHERE id=?", (args.id,))
    conn.commit()
    conn.close()
    print(f"{Fore.GREEN}Tache {args.id} faite ✓{Style.RESET_ALL}")
def cmd_del(args):
    conn = db.get_conn()
    conn.execute("DELETE FROM tasks WHERE id=?", (args.id,))
    conn.commit()
    conn.close()
    print(f"{Fore.RED}Tache {args.id} supprimee{Style.RESET_ALL}")
