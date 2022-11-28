/* ***************************
   készítette: név
   téma: kommentek, változók
   dátum: 2022-10-03
   verzió: v_1
   *************************** */

//A "System" alap osztályból, alapértelmezett névtérből behívjuk 
//a projekthez szükséges
//adatokat, beépített metódusokat
//Ide a feladattól függően szükséges nekem is beírnom a 
//System alosztályaiból
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//alapértelmezett névtér: osztályok, metódusok vannak benne
namespace elso
{
    //alapértelmezett osztály
    internal class Program
    {
        //alapértelmezett metódus, a program fő metódusa
        //void: nincs visszatérési értéke, paraméteres: string tömb argumentummal
        //ennek törzsébe írom a kódomat, ha nem OOP szemlélettel fejlesztek,
        //akkor csak ide írok
        //ha OOP szemléletet használok, akkor írok saját osztályokat, saját metódusokat
        static void Main(string[] args)
        {
            //konzolra kiiratás
            Console.WriteLine("Hello C#!");

            //változó deklarálása: lokális, mert csak az adott blokkban érhető el
            //OOP szemlélettel, a későbbiekben tudom a változók hatókörét
            //, elérhetőségét szabályozni
            String ido;
            String szep;

            //változó inicializálása: kezdő érték adás
            ido = "Ma reggel";
            szep = "szép az idő";

            Console.WriteLine(ido);
            Console.WriteLine(szep);

            //stringek összefűzése, konkatenációja: "+"
            Console.WriteLine(ido + " " + szep);

            //azonos típusú változók egy sorban deklarálhatók
            String eso, esernyo;
            eso = "Ha esik";
            esernyo = "viszek ernyőt";
            Console.WriteLine(eso + " " + esernyo);

            //deklarálás és inicializálás
            int x = 12;
            Console.WriteLine("x értéke:  " + x);

            //két szám összeadása
            int a, b, c;
            a = 4;
            b = 7;
            c = a + b;
            Console.WriteLine("a értéke:  " + a);
            Console.WriteLine("b értéke:  " + b);
            Console.WriteLine("az összeg: " + c);

            //konstans deklarálás, ÉS inicializálás(!)
            const int z = 10;

            //beolvasás konzolról
            //MINDEN, amit konzolról bekérek az STRING típus,
            //ezért konvertálnom kell(típuskonverzió)
            //, ehhez a "Parse(...)" metódust használhatom,
            //előtte meg kell adnom, milyen típusra akarok konvertálni
            Console.WriteLine("Adjon meg egy szamot: ");
            int szam = int.Parse(Console.ReadLine());
            Console.WriteLine("A bekért szám: " + szam);
            Console.WriteLine("A bekért szám típusa: " + szam.GetType());

            /*
             Feladat: kérd be a usertől a kör sugarát,
            ========  számítsd ki a kör kerületét és területét,
                      írd ki az eredményt
            */
            double pi_erteke = Math.PI;
            double ker, ter, r;
            Console.WriteLine("Add meg a kör sugarát: ");
            r = double.Parse(Console.ReadLine());
            ker = 2 * r * pi_erteke;
            ter = r * r * pi_erteke;
            Console.WriteLine("A kör kerülete: " + ker);
            Console.WriteLine("A kör területe: " + ter);

            /*
            OPERÁTOROK
            ==========
            
            ÖKÖLSZABÁLY: az operátoroknak van precedenciája,
                         az az művelet végrehajtási sorrendje,
                         ez programnyelvenként változhat
            EZÉRT ZÁRÓJELEZÜNK => így tudjuk szematikailag
            helyesen felépíteni az algoritmusainkat.
            
            
            1. matematikai operátorok:
            ===========================
            "<", ">", ">=", "<=", "==", "!=",
            "*", "/", "+", "-"
            maradékos osztás, modulo: "%"


            rövid forma:
            ============
            x = x + 10;
            x += 10;

            x = x + 1;
            ++x; x++;

            x = x - 1;
            --x; x--;


            2. logikai operátorok:
            ======================
            Ha a logikai változó értéke igaz, akkor ehhez "1" tartozik,
            Ha a logikai változó értéke hamis, akkor ehhez "0" tartozik.

            ÉS logikai művelet "and", "&&", IGAZSÁG TÁBLÁZATA
            *************************************************
            
            Két logikai változó ÉS kapcsolata akkor és csak akkor igaz,
            ha mindkét logikai változó értéke igaz.
            
            A   B   A&&B
            ============
            0   0   0
            0   1   0
            1   0   0
            1   1   1

            VAGY logikai művelet "or", "||", IGAZSÁG TÁBLÁZATA
            **************************************************
            Két logikai változó vagy kapcsolata akkor és csak akkor Hamis,
            ha mindkét logikai változó értéke hamis.

            A   B   A||B
            ============
            0   0   0
            0   1   1
            1   0   1
            1   1   1

            LOGIKAI TAGADÁS, negáció
            ========================
            Ha A értéke igaz, akkor A tagadása hamis, és fordítva

            A       "NEM A"
            ***************
            1       0
            0       1
             */

            /*
                    VEZÉRLÉSI SZERKEZETEK
                    =====================

            I. SZEKVENCIA
            =============
            Utasítások soros végrehajtása
            */

            string gyumolcs = "alma";
            Console.WriteLine("a gyümölcs neve " + gyumolcs);


            /*
            II. ELÁGAZÁSOK
            ==============
            Gyakran előfordul, hogy meg kell vizsgálnunk egy állítást, és attól
            függően, hogy igaz vagy hamis más-más utasítást kell végrehajtanunk.
            Ilyen esetben elágazást használunk
            */

            //IF szerkezet, "HA" - akkor

            int egesz = 10;

            if(egesz == 10) //fej rész, a logikai vizsgálatot tartalmazza
            { //törzs rész: azokat az utasításokat tartalmazza,
              //amiket a feltétel teljesülésével akarok végrehajtani
                Console.WriteLine("a szám értéke: " + egesz);
            }


            //IF - ELSE szerkezet, "HA" - akkor, "KÜLÖNBEN"

            string kedv = "vidám";

            if(kedv == "vidám")
            {
                Console.WriteLine("a kedvem: " + kedv);
            }
            else
            {
                Console.WriteLine("Nem vagyok vidám");
            }


            //ELSE - IF  szerkezet: több feltételt tudunk vele levizsgálni
            int egesz_szam = 12;

            if(egesz_szam == 12)
            {
                Console.WriteLine("a szám értéke: " + egesz_szam);
            }
            else if(egesz_szam == 10) //ELSE - IF-ből tetszőlegesen sokat írhatunk
            {
                Console.WriteLine("a szám értéke: 10");
            }
            else
            {
                Console.WriteLine("a szám értéke: nem tudom");
            }


            //SWITCH - CASE szerkezet
            //tetszőleges számú "case" írható,
            //a "break" kötelező, ezzel szakítod meg az adott ágat, ciklusokban is alkalmazhatom
            //a "default" az else ágnak felel meg

            string auto = "Volvo";

            switch(auto)
            {
                case "Volvo":
                    Console.WriteLine("Az autó Volvó");
                    break;
                case "BMW":
                    Console.WriteLine("Az autó BMW");
                    break;
                default:
                    Console.WriteLine("Az autó nem Volvó");
                    break;
            }

            /*
            III. CIKLUSOK
            =============
            Fajtái:

                - elöltesztelő (levizsgálja először a ciklusváltozó értékét, és ettől függően lehet nem fog lefutni): 
                    - for 
                    - kiterjesztett for: foreach
                    - while

                - számláló típus: 
                    - for
                    - kiterjesztett for: foreach
                    - while
            A for és a while egymással egyenértékű, ekvivalens

                - hátultesztelő (egyszer minenképpen lefut a ciklus mert a vizsgálat a végén van):
                    - do - while
             */


            //for ciklus, a ciklus változót a ciklus fejben deklaráljuk

            for(int i = 0; i < 10; i++)
            {
                Console.WriteLine("A ciklusváltozó: " + i);
            }


            //while ciklus, a ciklusváltozót a cikluson kívül deklaráljuk

            int j = 0;

            while(j < 24) //ciklusfejben fejben vizsgáljuk
            {
                Console.WriteLine("A ciklusváltozó: " + j);
                j++; //ciklusváltozó növelése, ha kimarad, akkor végtelen ciklusba kerülünk
            }


            //do - while

            int k = 4; //ciklus változó értékadás

            do
            {
                Console.WriteLine("A ciklusváltozó: " + k);
                k++; //ciklus változó növelés
            } while(k < 10); //ciklus feltétel

            //várakoztató utasítás
            Console.ReadKey();
        }
    }
}
