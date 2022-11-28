using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

/*
    Készíts el a másodfokú konzolos projektet, kérd be a usertől az egyenlet együtthatóit, ahol az egyenlet általános alapja "a * x2 + b * x1 + c"
    A megoldóképlet: x1 = (-b + négyzetgyök alatt b2 - 4 * a * c) / 2 * a
    x2 = (-b - négyzetgyök alatt b2 - 4 * a * c) / 2 * a
 */

namespace masodfoku
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Adja meg a másodfokú egyenlet együtthatóit!");

            Console .WriteLine();

            double a = 0;

            while(a == 0)
            {
                Console.Write("Kérem az a együtt ható értékét (nem lehet 0):");

                a = double.Parse(Console.ReadLine());
            }

            double b = 0;

            while (b == 0)
            {
                Console.Write("Kérem az b együtt ható értékét (nem lehet 0):");

                b = double.Parse(Console.ReadLine());
            }

            double c = 0;

            while (c == 0)
            {
                Console.Write("Kérem az c együtt ható értékét (nem lehet 0):");

                c = double.Parse(Console.ReadLine());
            }

            double x1 = (-b + Math.Sqrt(b * b) - 4 * a * c) / 2 * a;

            double x2 = (-b - Math.Sqrt(b * b) - 4 * a * c) / 2 * a;

            double masodfoku = a * x2 + b * x1 + c;

            Console.WriteLine();

            Console.WriteLine("Az eredmény: " + masodfoku);

            Console.ReadKey();
        }
    }
}
