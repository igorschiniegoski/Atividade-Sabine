"use client";

import Link from "next/link";
import { useActionState, useState } from "react";
import { UFS } from "@/lib/validacao/prestador";
import { salvarPrestador, type EstadoFormulario } from "./actions";

type Props = {
  id: number | null;
  inicial?: Record<string, string>;
};

export function FormularioPrestador({ id, inicial = {} }: Props) {
  const [estado, enviar, salvando] = useActionState<EstadoFormulario, FormData>(
    salvarPrestador.bind(null, id),
    {},
  );
  // depois de um erro o react limpa o formulario, entao os valores voltam da action
  const valor = (campo: string) => estado.valores?.[campo] ?? inicial[campo] ?? "";
  const erro = (campo: string) => estado.erros?.[campo]?.[0];

  const [tipo, setTipo] = useState(valor("tipo_pessoa") || "J");
  const juridica = tipo === "J";

  return (
    <form action={enviar} className="space-y-4" noValidate>
      {estado.mensagem && (
        <p className="rounded border-l-3 border-carimbo bg-carimbo-fundo px-3 py-2 text-sm text-carimbo" role="alert">
          {estado.mensagem}
        </p>
      )}

      <section className="cartao">
        <h2 className="cartao-titulo">Identificação</h2>
        <div className="grid gap-3 p-4 sm:grid-cols-2 lg:grid-cols-12">
          <div className="lg:col-span-3">
            <label htmlFor="tipo_pessoa" className="rotulo">
              Tipo <span className="text-carimbo">*</span>
            </label>
            <select id="tipo_pessoa" name="tipo_pessoa" value={tipo} onChange={(e) => setTipo(e.target.value)} className="campo">
              <option value="J">Pessoa jurídica</option>
              <option value="F">Pessoa física</option>
            </select>
          </div>
          <Campo nome="nome_razao_social" valor={valor("nome_razao_social")} erro={erro("nome_razao_social")} rotulo={juridica ? "Razão social" : "Nome completo"} obrigatorio className="sm:col-span-2 lg:col-span-5" />
          <Campo
            nome="cpf_cnpj"
            valor={valor("cpf_cnpj")}
            erro={erro("cpf_cnpj")}
            rotulo={juridica ? "CNPJ" : "CPF"}
            obrigatorio
            className="lg:col-span-4"
            placeholder={juridica ? "00.000.000/0000-00" : "000.000.000-00"}
          />
          <Campo
            nome="nome_fantasia"
            valor={valor("nome_fantasia")}
            erro={erro("nome_fantasia")}
            rotulo={juridica ? "Nome fantasia" : "Como é conhecido"}
            className="lg:col-span-4"
            ajuda="Aparece abaixo do nome na listagem."
          />
          <Campo nome="telefone" valor={valor("telefone")} erro={erro("telefone")} rotulo="Telefone" obrigatorio className="lg:col-span-4" placeholder="(44) 99999-9999" />
          <Campo
            nome="email"
            valor={valor("email")}
            erro={erro("email")}
            rotulo="E-mail"
            type="email"
            className="sm:col-span-2 lg:col-span-4"
            ajuda="Usado também para liberar o acesso do prestador ao sistema."
          />
        </div>
      </section>

      <section className="cartao">
        <h2 className="cartao-titulo">Endereço</h2>
        <div className="grid gap-3 p-4 sm:grid-cols-2 lg:grid-cols-12">
          <Campo nome="cep" valor={valor("cep")} erro={erro("cep")} rotulo="CEP" obrigatorio className="lg:col-span-3" placeholder="00000-000" />
          <Campo nome="logradouro" valor={valor("logradouro")} erro={erro("logradouro")} rotulo="Logradouro" obrigatorio className="lg:col-span-6" />
          <Campo nome="numero" valor={valor("numero")} erro={erro("numero")} rotulo="Número" obrigatorio className="lg:col-span-3" />
          <Campo nome="complemento" valor={valor("complemento")} erro={erro("complemento")} rotulo="Complemento" className="lg:col-span-3" />
          <Campo nome="bairro" valor={valor("bairro")} erro={erro("bairro")} rotulo="Bairro" obrigatorio className="lg:col-span-4" />
          <Campo nome="cidade" valor={valor("cidade")} erro={erro("cidade")} rotulo="Cidade" obrigatorio className="lg:col-span-3" />
          <div className="lg:col-span-2">
            <label htmlFor="uf" className="rotulo">
              UF <span className="text-carimbo">*</span>
            </label>
            <select id="uf" name="uf" defaultValue={valor("uf") || "PR"} className={`campo ${erro("uf") ? "campo-erro" : ""}`}>
              {UFS.map((uf) => (
                <option key={uf} value={uf}>{uf}</option>
              ))}
            </select>
          </div>
        </div>
        <div className="flex justify-end gap-2 border-t border-regua-clara px-4 py-3">
          <Link href="/prestadores" className="botao">Cancelar</Link>
          <button type="submit" disabled={salvando} className="botao-principal">
            {salvando ? "Salvando..." : "Salvar"}
          </button>
        </div>
      </section>
    </form>
  );
}

type PropsCampo = {
  nome: string;
  rotulo: string;
  valor: string;
  erro?: string;
  obrigatorio?: boolean;
  ajuda?: string;
  className?: string;
  type?: string;
  placeholder?: string;
};

function Campo(props: PropsCampo) {
  return (
    <div className={props.className}>
      <label htmlFor={props.nome} className="rotulo">
        {props.rotulo} {props.obrigatorio && <span className="text-carimbo">*</span>}
      </label>
      <input
        id={props.nome}
        name={props.nome}
        type={props.type ?? "text"}
        defaultValue={props.valor}
        placeholder={props.placeholder}
        aria-invalid={!!props.erro}
        className={`campo ${props.erro ? "campo-erro" : ""}`}
      />
      {props.erro && <p className="msg-erro">{props.erro}</p>}
      {!props.erro && props.ajuda && <p className="mt-1 text-xs text-tinta2">{props.ajuda}</p>}
    </div>
  );
}
