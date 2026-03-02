---
layout: default
title: LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics
---

# LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mathematics
**arXiv**：[2602.24173v1](https://arxiv.org/abs/2602.24173) · [PDF](https://arxiv.org/pdf/2602.24173.pdf)  
**作者**：Antoine Peyronnet, Fabian Gloeckle, Amaury Hayat  

**一句话要点**：提出LemmaBench以评估大语言模型在数学研究中的能力

**关键词**：数学基准, 大语言模型评估, 定理证明, arXiv数据, 自动管道, 研究级数学

## 3 点简述
- 现有基准依赖静态问题，无法反映最新数学研究水平
- 通过自动管道从arXiv提取引理并重写为自包含陈述，建立可更新基准
- 实验显示当前模型在定理证明中准确率约10-15%，与人类水平差距较大

## 摘要（原文）

> We present a new approach for benchmarking Large Language Model (LLM) capabilities on research-level mathematics. Existing benchmarks largely rely on static, hand-curated sets of contest or textbook-style problems as proxies for mathematical research. Instead, we establish an updatable benchmark evaluating models directly on the latest research results in mathematics. This consists of an automatic pipeline that extracts lemmas from arXiv and rewrites them into self-contained statements by making all assumptions and required definitions explicit. It results in a benchmark that can be updated regularly with new problems taken directly from human mathematical research, while previous instances can be used for training without compromising future evaluations. We benchmark current state-of-the-art LLMs, which obtain around 10-15$\%$ accuracy in theorem proving (pass@1) depending on the model, showing that there is currently a large margin of progression for LLMs to reach human-level proving capabilities in a research context.

