---
layout: default
title: ProtoFlow: Interpretable and Robust Surgical Workflow Modeling with Learned Dynamic Scene Graph Prototypes
---

# ProtoFlow: Interpretable and Robust Surgical Workflow Modeling with Learned Dynamic Scene Graph Prototypes
**arXiv**：[2512.14092v1](https://arxiv.org/abs/2512.14092) · [PDF](https://arxiv.org/pdf/2512.14092.pdf)  
**作者**：Felix Holm, Ghazal Ghazaei, Nassir Navab  

**一句话要点**：提出ProtoFlow框架，通过动态场景图原型学习实现可解释且鲁棒的手术工作流建模

**关键词**：手术工作流建模, 动态场景图, 原型学习, 图神经网络, 可解释AI, 少样本学习

## 3 点简述
- 核心问题：手术识别面临高标注成本、数据稀缺和模型可解释性不足的挑战
- 方法要点：结合自监督预训练和原型微调，学习动态场景图原型以捕获手术交互模式
- 实验或效果：在CAT-SG数据集上超越基线，在少样本场景中表现鲁棒，原型提供可解释洞察

## 摘要（原文）

> Purpose: Detailed surgical recognition is critical for advancing AI-assisted surgery, yet progress is hampered by high annotation costs, data scarcity, and a lack of interpretable models. While scene graphs offer a structured abstraction of surgical events, their full potential remains untapped. In this work, we introduce ProtoFlow, a novel framework that learns dynamic scene graph prototypes to model complex surgical workflows in an interpretable and robust manner.
>   Methods: ProtoFlow leverages a graph neural network (GNN) encoder-decoder architecture that combines self-supervised pretraining for rich representation learning with a prototype-based fine-tuning stage. This process discovers and refines core prototypes that encapsulate recurring, clinically meaningful patterns of surgical interaction, forming an explainable foundation for workflow analysis.
>   Results: We evaluate our approach on the fine-grained CAT-SG dataset. ProtoFlow not only outperforms standard GNN baselines in overall accuracy but also demonstrates exceptional robustness in limited-data, few-shot scenarios, maintaining strong performance when trained on as few as one surgical video. Our qualitative analyses further show that the learned prototypes successfully identify distinct surgical sub-techniques and provide clear, interpretable insights into workflow deviations and rare complications.
>   Conclusion: By uniting robust representation learning with inherent explainability, ProtoFlow represents a significant step toward developing more transparent, reliable, and data-efficient AI systems, accelerating their potential for clinical adoption in surgical training, real-time decision support, and workflow optimization.

