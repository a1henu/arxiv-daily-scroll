---
layout: default
title: OPBench: A Graph Benchmark to Combat the Opioid Crisis
---

# OPBench: A Graph Benchmark to Combat the Opioid Crisis
**arXiv**：[2602.14602v1](https://arxiv.org/abs/2602.14602) · [PDF](https://arxiv.org/pdf/2602.14602.pdf)  
**作者**：Tianyi Ma, Yiyang Li, Yiyue Qian, Zheyuan Zhang, Zehong Wang, Chuxu Zhang, Yanfang Ye  

**一句话要点**：提出OPBench图基准以应对阿片类药物危机，涵盖三个关键应用领域。

**关键词**：图学习基准, 阿片类药物危机, 异构图, 超图, 药物滥用预测, 数据隐私

## 3 点简述
- 核心问题：缺乏针对阿片类药物危机的图学习方法综合基准，阻碍方法评估与比较。
- 方法要点：构建包含五个数据集的基准，覆盖医疗索赔、数字平台和饮食模式等场景，采用异构图和超图结构。
- 实验或效果：通过统一评估框架和基线实验，分析现有图学习方法的优缺点，提供未来研究见解。

## 摘要（原文）

> The opioid epidemic continues to ravage communities worldwide, straining healthcare systems, disrupting families, and demanding urgent computational solutions. To combat this lethal opioid crisis, graph learning methods have emerged as a promising paradigm for modeling complex drug-related phenomena. However, a significant gap remains: there is no comprehensive benchmark for systematically evaluating these methods across real-world opioid crisis scenarios. To bridge this gap, we introduce OPBench, the first comprehensive opioid benchmark comprising five datasets across three critical application domains: opioid overdose detection from healthcare claims, illicit drug trafficking detection from digital platforms, and drug misuse prediction from dietary patterns. Specifically, OPBench incorporates diverse graph structures, including heterogeneous graphs and hypergraphs, to preserve the rich and complex relational information among drug-related data. To address data scarcity, we collaborate with domain experts and authoritative institutions to curate and annotate datasets while adhering to privacy and ethical guidelines. Furthermore, we establish a unified evaluation framework with standardized protocols, predefined data splits, and reproducible baselines to facilitate fair and systematic comparison among graph learning methods. Through extensive experiments, we analyze the strengths and limitations of existing graph learning methods, thereby providing actionable insights for future research in combating the opioid crisis. Our source code and datasets are available at https://github.com/Tianyi-Billy-Ma/OPBench.

