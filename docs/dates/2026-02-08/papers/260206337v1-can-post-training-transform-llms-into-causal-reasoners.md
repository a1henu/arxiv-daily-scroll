---
layout: default
title: Can Post-Training Transform LLMs into Causal Reasoners?
---

# Can Post-Training Transform LLMs into Causal Reasoners?
**arXiv**：[2602.06337v1](https://arxiv.org/abs/2602.06337) · [PDF](https://arxiv.org/pdf/2602.06337.pdf)  
**作者**：Junqi Chen, Sirui Chen, Chaochao Lu  

**一句话要点**：提出CauGym数据集与后训练方法，提升LLMs因果推理能力

**关键词**：因果推理, 后训练, 大型语言模型, 数据集构建, 泛化能力, 鲁棒性

## 3 点简述
- 研究后训练对LLMs因果推理能力的影响，填补探索不足的空白
- 引入CauGym数据集，包含七个核心因果任务和五个测试集，用于系统评估
- 实验显示后训练使较小LLMs在因果推理上超越更大模型，并展现强泛化性

## 摘要（原文）

> Causal inference is essential for decision-making but remains challenging for non-experts. While large language models (LLMs) show promise in this domain, their precise causal estimation capabilities are still limited, and the impact of post-training on these abilities is insufficiently explored. This paper examines the extent to which post-training can enhance LLMs' capacity for causal inference. We introduce CauGym, a comprehensive dataset comprising seven core causal tasks for training and five diverse test sets. Using this dataset, we systematically evaluate five post-training approaches: SFT, DPO, KTO, PPO, and GRPO. Across five in-domain and four existing benchmarks, our experiments demonstrate that appropriate post-training enables smaller LLMs to perform causal inference competitively, often surpassing much larger models. Our 14B parameter model achieves 93.5% accuracy on the CaLM benchmark, compared to 55.4% by OpenAI o3. Furthermore, the post-trained LLMs exhibit strong generalization and robustness under real-world conditions such as distribution shifts and noisy data. Collectively, these findings provide the first systematic evidence that targeted post-training can produce reliable and robust LLM-based causal reasoners. Our data and GRPO-model are available at https://github.com/OpenCausaLab/CauGym.

