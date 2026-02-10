---
layout: default
title: PBLean: Pseudo-Boolean Proof Certificates for Lean 4
---

# PBLean: Pseudo-Boolean Proof Certificates for Lean 4
**arXiv**：[2602.08692v1](https://arxiv.org/abs/2602.08692) · [PDF](https://arxiv.org/pdf/2602.08692.pdf)  
**作者**：Stefan Szeider  

**一句话要点**：提出PBLean方法，将VeriPB伪布尔证明证书导入Lean 4，通过反射实现高效验证并生成可组合定理。

**关键词**：伪布尔证明, Lean 4集成, 反射验证, 证明证书, 组合问题, 形式化验证

## 3 点简述
- 核心问题：传统伪布尔证明证书在Lean中显式构建证明项时内存消耗大，难以处理大规模证明。
- 方法要点：采用反射技术，在Lean中完全证明布尔检查器函数，编译为原生代码执行，支持VeriPB所有内核规则。
- 实验或效果：方法可处理数万步证明，避免内存耗尽，并通过验证编码确保约束翻译正确性，应用于组合问题。

## 摘要（原文）

> We present PBLean, a method for importing VeriPB pseudo-Boolean (PB) proof certificates into Lean 4. Key to our approach is reflection: a Boolean checker function whose soundness is fully proved in Lean and executed as compiled native code. Our method scales to proofs with tens of thousands of steps that would exhaust memory under explicit proof-term construction. Our checker supports all VeriPB kernel rules, including cutting-plane derivations and proof-by-contradiction subproofs. In contrast to external verified checkers that produce verdicts, our integration yields Lean theorems that can serve as composable lemmas in larger formal developments. To derive theorems about the original combinatorial problems rather than about PB constraints alone, we support verified encodings. This closes the trust gap between solver output and problem semantics since the constraint translation and its correctness proof are both formalized in Lean. We demonstrate the approach on various combinatorial problems.

