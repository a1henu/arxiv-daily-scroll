---
layout: default
title: From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection
---

# From Lab to Reality: A Practical Evaluation of Deep Learning Models and LLMs for Vulnerability Detection
**arXiv**：[2512.10485v1](https://arxiv.org/abs/2512.10485) · [PDF](https://arxiv.org/pdf/2512.10485.pdf)  
**作者**：Chaomeng Lu, Bert Lagaisse  

**一句话要点**：评估深度学习与LLM在漏洞检测中的实际应用，揭示学术基准与现实部署间的差距

**关键词**：漏洞检测, 深度学习模型, 大语言模型, 泛化评估, 代码表示分析, 部署框架

## 3 点简述
- 核心问题：深度学习模型在基准数据集上表现良好，但真实世界有效性未知，存在泛化挑战
- 方法要点：系统评估ReVeal和LineVul模型，结合LLMs在VentiVul数据集上进行部署测试
- 实验或效果：模型在表示空间难以区分漏洞，跨数据集泛化差，VentiVul上性能大幅下降

## 摘要（原文）

> Vulnerability detection methods based on deep learning (DL) have shown strong performance on benchmark datasets, yet their real-world effectiveness remains underexplored. Recent work suggests that both graph neural network (GNN)-based and transformer-based models, including large language models (LLMs), yield promising results when evaluated on curated benchmark datasets. These datasets are typically characterized by consistent data distributions and heuristic or partially noisy labels. In this study, we systematically evaluate two representative DL models-ReVeal and LineVul-across four representative datasets: Juliet, Devign, BigVul, and ICVul. Each model is trained independently on each respective dataset, and their code representations are analyzed using t-SNE to uncover vulnerability related patterns. To assess realistic applicability, we deploy these models along with four pretrained LLMs, Claude 3.5 Sonnet, GPT-o3-mini, GPT-4o, and GPT-5 on a curated dataset, VentiVul, comprising 20 recently (May 2025) fixed vulnerabilities from the Linux kernel. Our experiments reveal that current models struggle to distinguish vulnerable from non-vulnerable code in representation space and generalize poorly across datasets with differing distributions. When evaluated on VentiVul, our newly constructed time-wise out-of-distribution dataset, performance drops sharply, with most models failing to detect vulnerabilities reliably. These results expose a persistent gap between academic benchmarks and real-world deployment, emphasizing the value of our deployment-oriented evaluation framework and the need for more robust code representations and higher-quality datasets.

