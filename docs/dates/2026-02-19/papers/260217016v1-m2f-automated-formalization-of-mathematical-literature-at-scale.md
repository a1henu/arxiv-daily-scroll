---
layout: default
title: M2F: Automated Formalization of Mathematical Literature at Scale
---

# M2F: Automated Formalization of Mathematical Literature at Scale
**arXiv**：[2602.17016v1](https://arxiv.org/abs/2602.17016) · [PDF](https://arxiv.org/pdf/2602.17016.pdf)  
**作者**：Zichen Wang, Wanli Ma, Zhenyu Ming, Gong Zhang, Kun Yuan, Zaiwen Wen  

**一句话要点**：提出M2F框架，实现数学文献到Lean代码的端到端项目级自动形式化。

**关键词**：自动形式化, 数学文献, Lean定理证明, 项目级编译, 代理框架, 证明修复

## 3 点简述
- 核心问题：数学文献自动形式化局限于片段，难以扩展到教科书和论文等长文本。
- 方法要点：采用两阶段代理框架，先编译声明骨架再修复证明，保持验证器在循环中。
- 实验或效果：在约三周内将479页教科书形式化为15万行Lean代码，证明成功率96%。

## 摘要（原文）

> Automated formalization of mathematics enables mechanical verification but remains limited to isolated theorems and short snippets. Scaling to textbooks and research papers is largely unaddressed, as it requires managing cross-file dependencies, resolving imports, and ensuring that entire projects compile end-to-end. We present M2F (Math-to-Formal), the first agentic framework for end-to-end, project-scale autoformalization in Lean. The framework operates in two stages. The statement compilation stage splits the document into atomic blocks, orders them via inferred dependencies, and repairs declaration skeletons until the project compiles, allowing placeholders in proofs. The proof repair stage closes these holes under fixed signatures using goal-conditioned local edits. Throughout both stages, M2F keeps the verifier in the loop, committing edits only when toolchain feedback confirms improvement. In approximately three weeks, M2F converts long-form mathematical sources into a project-scale Lean library of 153,853 lines from 479 pages textbooks on real analysis and convex analysis, fully formalized as Lean declarations with accompanying proofs. This represents textbook-scale formalization at a pace that would typically require months or years of expert effort. On FATE-H, we achieve $96\%$ proof success (vs.\ $80\%$ for a strong baseline). Together, these results demonstrate that practical, large-scale automated formalization of mathematical literature is within reach. The full generated Lean code from our runs is available at https://github.com/optsuite/ReasBook.git.

