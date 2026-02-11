---
layout: default
title: AlgoVeri: An Aligned Benchmark for Verified Code Generation on Classical Algorithms
---

# AlgoVeri: An Aligned Benchmark for Verified Code Generation on Classical Algorithms
**arXiv**：[2602.09464v1](https://arxiv.org/abs/2602.09464) · [PDF](https://arxiv.org/pdf/2602.09464.pdf)  
**作者**：Haoyu Zhao, Ziran Yang, Jiawei Li, Deyuan He, Zenan Li, Chi Jin, Venugopal V. Veeravalli, Aarti Gupta, Sanjeev Arora  

**一句话要点**：提出AlgoVeri基准以解决跨范式验证代码生成评估不统一的问题

**关键词**：验证代码生成, 形式化验证, 算法基准, 跨范式评估, 语言设计影响

## 3 点简述
- 现有验证代码生成基准仅测试单一语言/工具，性能指标不可直接比较
- AlgoVeri通过77个经典算法的相同功能合约，在Dafny、Verus和Lean中评估验证代码生成
- 实验揭示前沿模型在不同验证系统中的能力差距，如Dafny成功率40.3%，Verus为24.7%，Lean仅7.8%

## 摘要（原文）

> Vericoding refers to the generation of formally verified code from rigorous specifications. Recent AI models show promise in vericoding, but a unified methodology for cross-paradigm evaluation is lacking. Existing benchmarks test only individual languages/tools (e.g., Dafny, Verus, and Lean) and each covers very different tasks, so the performance numbers are not directly comparable. We address this gap with AlgoVeri, a benchmark that evaluates vericoding of $77$ classical algorithms in Dafny, Verus, and Lean. By enforcing identical functional contracts, AlgoVeri reveals critical capability gaps in verification systems. While frontier models achieve tractable success in Dafny ($40.3$% for Gemini-3 Flash), where high-level abstractions and SMT automation simplify the workflow, performance collapses under the systems-level memory constraints of Verus ($24.7$%) and the explicit proof construction required by Lean (7.8%). Beyond aggregate metrics, we uncover a sharp divergence in test-time compute dynamics: Gemini-3 effectively utilizes iterative repair to boost performance (e.g., tripling pass rates in Dafny), whereas GPT-OSS saturates early. Finally, our error analysis shows that language design affects the refinement trajectory: while Dafny allows models to focus on logical correctness, Verus and Lean trap models in persistent syntactic and semantic barriers. All data and evaluation code can be found at https://github.com/haoyuzhao123/algoveri.

