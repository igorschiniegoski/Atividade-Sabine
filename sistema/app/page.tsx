import { redirect } from "next/navigation";

// por enquanto a unica area pronta e a de prestadores (recorte da entrega de 20/10)
export default function Inicio() {
  redirect("/prestadores");
}
