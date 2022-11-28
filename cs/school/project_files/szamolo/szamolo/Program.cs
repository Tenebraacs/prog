using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace szamolo
{
    internal class Program
    {
        static void Main(string[] args)
        {

            /*
             Feladat: 1.) Készíts C# konzolos alkalmazást, amely menüválasztással az alábbi feladatokat
             végzi el:
                1.) Derékszögű háromszög szerkezthető-e az adatokból?
                2.) elsőfokú egyenlet megoldó program
                3.) Páros számok 1-121 között
                4.) 7-el osztható számok 71-200 között
                5.) 7-el osztható, páros számok 71-200 között
				
			Kérd be a usertől az általa választott feladat számát, 
			és annak megfelelően fusson le a programod.
			Ha nem megfelelő számot ad, tájékoztasd, hogy 
			nem megfelelő számot adott meg, és zárd be a konzolt.
			
			Mentsd el a "Program.cs" állományt "monogram_alapfeladatok_v2.cs" néven,
			és add be a mai alkalom végéig a "!bead/2022-10-24" mappába. Egy jegyet kapsz rá.
			
		 2.) Valósítsd meg az 1.) -es feladatot pythonban és és add be a mai alkalom végéig
		     a "!bead/2022-10-24" mappába "monogram_alapfeladatok_v2.py" néven. Egy jegyet kapsz rá.
             */

            Console.WriteLine("Válasszon az alábbi opciók közül");
            Console.WriteLine("1.) Derékszögű háromszög szerkezthető-e az adatokból?");
            Console.WriteLine("2.) Elsőfokú egyenlet megoldó program");
            Console.WriteLine("3.) Páros számok 1-121 között");
            Console.WriteLine("4.) 7-el osztható számok 71-200 között");
            Console.WriteLine("5.) 7-el osztható, páros számok 71-200 között");

            double opcio;
            opcio = double.Parse(Console.ReadLine());
            if(opcio == 1)
            {
                Console.WriteLine("Derékszögű-e a háromszög?");
                double A, B, C, a, b, c, derekszog;
                Console.WriteLine("Adja meg az 'a' oldal hosszát: ");
                A = double.Parse(Console.ReadLine());
                Console.WriteLine("Adja meg a 'b' oldal hosszát: ");
                B = double.Parse(Console.ReadLine());
                Console.WriteLine("Adja meg a 'c' oldal hosszát: ");
                C = double.Parse(Console.ReadLine());
                if (A > C)
                {
                    c = A;
                    b = B;
                    a = C;
                }else if(B > C) 
                {
                    c = B;
                    a = A;
                    b = C;
                }else
                {
                    a = A;
                    b = B;
                    c = C;
                }
                derekszog = a * a + b * b;
                if(derekszog == c * c)
                {
                    Console.WriteLine("Ez egy derékszögű háromszög");
                }else
                {
                    Console.WriteLine("Ez nem egy derékszögű háromszög");
                }
            }
            else if(opcio == 2)
            {
                Console.WriteLine("Az X kiszámítása elsőfokú egyenletben");
                double m, b, x;
                Console.WriteLine("Adja meg az 'm' értéket:");
                m = double.Parse(Console.ReadLine());
                Console.WriteLine("Adja meg a 'b' értéket:");
                b = double.Parse(Console.ReadLine());
                x = -(b / m);
                Console.WriteLine("Az 'x' értke: " + x);
            }
            else if(opcio == 3)
            {
                Console.WriteLine("Az 1 és 121 közötti páros számok:");
                for (int i = 1; i < 121; i++)
                {
                    if (i % 2 == 0)
                    {
                        Console.WriteLine(i);
                    }
                }
            }
            else if(opcio == 4)
            {
                Console.WriteLine("A 71 és 200 között 7-el osztható számok:");
                for (int i = 71; i < 200; i++)
                {
                    if (i % 7 == 0)
                    {
                        Console.WriteLine(i);
                    }
                }
            }
            else if(opcio == 5)
            {
                Console.WriteLine("A 71 és 200 között 7-el osztható páros számok:");
                for (int i = 71; i < 200; i++)
                {
                    if (i % 7 == 0)
                    {
                        if(i % 2 == 0)
                        {
                            Console.WriteLine(i);
                        }
                    }
                }
            }
            else
            {
                Console.WriteLine("A megadott opció helytelen.");
            }
            Console.WriteLine("Nyomjon egy gombot a konzol bezárásához.");
            Console.ReadKey();
        }
    }
}
