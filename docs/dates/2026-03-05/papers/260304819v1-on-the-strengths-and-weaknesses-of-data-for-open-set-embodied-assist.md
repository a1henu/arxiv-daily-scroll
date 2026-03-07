---
layout: default
title: On the Strengths and Weaknesses of Data for Open-set Embodied Assistance
---

# On the Strengths and Weaknesses of Data for Open-set Embodied Assistance
**arXiv**：[2603.04819v1](https://arxiv.org/abs/2603.04819) · [PDF](https://arxiv.org/pdf/2603.04819.pdf)  
**作者**：Pradyumna Tambwekar, Andrew Silva, Deepak Gopinath, Jonathan DeCastro, Xiongyi Cui, Guy Rosman  

**一句话要点**：提出基于多样化交互数据的多模态基础模型，以解决开放集具身辅助中的泛化问题。

**关键词**：具身辅助, 开放集泛化, 多模态基础模型, 交互数据生成, 合成数据集

## 3 点简述
- 研究开放集纠正辅助任务，要求模型在未见用户行为和新配置下提供纠正或语言反馈。
- 在Overcooked中生成合成辅助数据集，微调LLaMA模型评估泛化能力。
- 发现性能模型受益于覆盖多模态接地、缺陷推断和多样化场景的数据集。

## 摘要（原文）

> Embodied foundation models are increasingly performant in real-world domains such as robotics or autonomous driving. These models are often deployed in interactive or assistive settings, where it is important that these assistive models generalize to new users and new tasks. Diverse interactive data generation offers a promising avenue for providing data-efficient generalization capabilities for interactive embodied foundation models. In this paper, we investigate the generalization capabilities of a multimodal foundation model fine-tuned on diverse interactive assistance data in a synthetic domain. We explore generalization along two axes: a) assistance with unseen categories of user behavior and b) providing guidance in new configurations not encountered during training. We study a broad capability called \textbf{Open-Set Corrective Assistance}, in which the model needs to inspect lengthy user behavior and provide assistance through either corrective actions or language-based feedback. This task remains unsolved in prior work, which typically assumes closed corrective categories or relies on external planners, making it a challenging testbed for evaluating the limits of assistive data. To support this task, we generate synthetic assistive datasets in Overcooked and fine-tune a LLaMA-based model to evaluate generalization to novel tasks and user behaviors. Our approach provides key insights into the nature of assistive datasets required to enable open-set assistive intelligence. In particular, we show that performant models benefit from datasets that cover different aspects of assistance, including multimodal grounding, defect inference, and exposure to diverse scenarios.

