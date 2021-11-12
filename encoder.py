# 5w
# b50513bda99c8f216b3490bdabd76c7fa3f10eb2ab72a2f7367e1b466c5b742b7dc5a492af55356cb006a53b7347752846bb42a199bf694ecab49c108c5ad09d
import typer
from Password import Password
import time
import os


app = typer.Typer()


@app.command()
def random(count_symbols: int = 2, pin_code: str = '0000',
           check_summa: str = 'b50513bda99c8f216b3490bdabd76c7fa3f10eb2ab72a2f7367e1b466c5b742b7dc5a492af55356cb006a53b7347752846bb42a199bf694ecab49c108c5ad09d'):
    typer.echo(f'Количество доступных символов: {count_symbols}')
    typer.echo(f'Пин код: {pin_code}')
    typer.echo(f'Ключ пароля: {check_summa}')

    start_time = time.time()
    count_random = 0

    while True:
        count_random += 1
        password = Password()
        password.generation(int(count_symbols), pin_code)

        typer.echo(f'Проверяем пароль: {password.password}')

        if check_summa == password.check_summa:
            typer.echo(f'Совпадение: {password.password}')
            typer.echo(f'Количество пройденных вариантов: {count_random}')
            typer.echo(f'Время перебора составило: {time.time() - start_time}')

            break
        else:
            os.system('cls||clear')


if __name__ == "__main__":
    app()
