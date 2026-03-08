---
layout: default
title: On the Strengths and Weaknesses of Data for Open-set Embodied Assistance
---

# On the Strengths and Weaknesses of Data for Open-set Embodied Assistance
**arXiv**：[2603.04819v1](https://arxiv.org/abs/2603.04819) · [PDF](https://arxiv.org/pdf/2603.04819.pdf)  
**作者**：Pradyumna Tambwekar, Andrew Silva, Deepak Gopinath, Jonathan DeCastro, Xiongyi Cui, Guy Rosman  

**一句话要点**：研究多样化交互数据对开放集具身辅助模型泛化能力的影响

**关键词**：具身基础模型, 开放集辅助, 数据泛化, 多模态学习, 合成数据集

## 3 点简述
- 核心问题：开放集纠正辅助任务中，模型需泛化至未见用户行为和新配置。
- 方法要点：在Overcooked中生成合成辅助数据集，微调LLaMA模型评估泛化能力。
- 实验或效果：发现性能模型受益于覆盖多模态接地、缺陷推断和多样场景的数据集。

## 摘要（原文）

> Embodied foundation models are increasingly performant in real-world domains such as robotics or autonomous driving. These models are often deployed in interactive or assistive settings, where it is important that these assistive models generalize to new users and new tasks. Diverse interactive data generation offers a promising avenue for providing data-efficient generalization capabilities for interactive embodied foundation models. In this paper, we investigate the generalization capabilities of a multimodal foundation model fine-tuned on diverse interactive assistance data in a synthetic domain. We explore generalization along two axes: a) assistance with unseen categories of user behavior and b) providing guidance in new configurations not encountered during training. We study a broad capability called \textbf{Open-Set Corrective Assistance}, in which the model needs to inspect lengthy user behavior and provide assistance through either corrective actions or language-based feedback. This task remains unsolved in prior work, which typically assumes closed corrective categories or relies on external planners, making it a challenging testbed for evaluating the limits of assistive data. To support this task, we generate synthetic assistive datasets in Overcooked and fine-tune a LLaMA-based model to evaluate generalization to novel tasks and user behaviors. Our approach provides key insights into the nature of assistive datasets required to enable open-set assistive intelligence. In particular, we show that performant models benefit from datasets that cover different aspects of assistance, including multimodal grounding, defect inference, and exposure to diverse scenarios.

