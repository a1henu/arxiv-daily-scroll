---
layout: default
title: Task-Specific Sparse Feature Masks for Molecular Toxicity Prediction with Chemical Language Models
---

# Task-Specific Sparse Feature Masks for Molecular Toxicity Prediction with Chemical Language Models
**arXiv**：[2512.11412v1](https://arxiv.org/abs/2512.11412) · [PDF](https://arxiv.org/pdf/2512.11412.pdf)  
**作者**：Kwun Sy Lee, Jiawei Chen, Fuk Sheng Ford Chung, Tianyu Zhao, Zhenyuan Chen, Debby D. Wang  

**一句话要点**：提出任务特定稀疏特征掩码的多任务学习框架，以提升分子毒性预测的准确性和可解释性。

**关键词**：分子毒性预测, 多任务学习, 化学语言模型, 稀疏注意力, 可解释性, 药物发现

## 3 点简述
- 核心问题：现有分子毒性预测模型为黑盒，缺乏可验证的结构洞察，阻碍高安全决策应用。
- 方法要点：结合共享化学语言模型与任务特定注意力模块，通过L1稀疏惩罚聚焦关键分子片段。
- 实验或效果：在ClinTox、SIDER和Tox21数据集上优于单任务和标准多任务基线，并提供化学直观可视化。

## 摘要（原文）

> Reliable in silico molecular toxicity prediction is a cornerstone of modern drug discovery, offering a scalable alternative to experimental screening. However, the black-box nature of state-of-the-art models remains a significant barrier to adoption, as high-stakes safety decisions demand verifiable structural insights alongside predictive performance. To address this, we propose a novel multi-task learning (MTL) framework designed to jointly enhance accuracy and interpretability. Our architecture integrates a shared chemical language model with task-specific attention modules. By imposing an L1 sparsity penalty on these modules, the framework is constrained to focus on a minimal set of salient molecular fragments for each distinct toxicity endpoint. The resulting framework is trained end-to-end and is readily adaptable to various transformer-based backbones. Evaluated on the ClinTox, SIDER, and Tox21 benchmark datasets, our approach consistently outperforms both single-task and standard MTL baselines. Crucially, the sparse attention weights provide chemically intuitive visualizations that reveal the specific fragments influencing predictions, thereby enhancing insight into the model's decision-making process.

