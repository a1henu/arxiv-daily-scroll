---
layout: default
title: OptiMAG: Structure-Semantic Alignment via Unbalanced Optimal Transport
---

# OptiMAG: Structure-Semantic Alignment via Unbalanced Optimal Transport
**arXiv**：[2601.22856v1](https://arxiv.org/abs/2601.22856) · [PDF](https://arxiv.org/pdf/2601.22856.pdf)  
**作者**：Yilong Zuo, Xunkai Li, Zhihan Zhang, Qiangqiang Dai, Ronghua Li, Guoren Wang  

**一句话要点**：提出OptiMAG框架，通过不平衡最优传输解决多模态属性图中结构与语义不一致问题。

**关键词**：多模态属性图, 最优传输, 结构语义对齐, 图神经网络, 跨模态学习, 正则化框架

## 3 点简述
- 核心问题：多模态属性图中显式图结构与模态嵌入诱导的隐式语义结构存在冲突，导致消息传递时聚合噪声。
- 方法要点：使用融合Gromov-Wasserstein距离正则化局部邻域跨模态结构一致性，并引入KL散度惩罚自适应处理不一致。
- 实验或效果：在节点分类、链接预测及图到文本/图像生成等任务中优于基线，可作为即插即用正则器集成到现有模型。

## 摘要（原文）

> Multimodal Attributed Graphs (MAGs) have been widely adopted for modeling complex systems by integrating multi-modal information, such as text and images, on nodes. However, we identify a discrepancy between the implicit semantic structure induced by different modality embeddings and the explicit graph structure. For instance, neighbors in the explicit graph structure may be close in one modality but distant in another. Since existing methods typically perform message passing over the fixed explicit graph structure, they inadvertently aggregate dissimilar features, introducing modality-specific noise and impeding effective node representation learning. To address this, we propose OptiMAG, an Unbalanced Optimal Transport-based regularization framework. OptiMAG employs the Fused Gromov-Wasserstein distance to explicitly guide cross-modal structural consistency within local neighborhoods, effectively mitigating structural-semantic conflicts. Moreover, a KL divergence penalty enables adaptive handling of cross-modal inconsistencies. This framework can be seamlessly integrated into existing multimodal graph models, acting as an effective drop-in regularizer. Experiments demonstrate that OptiMAG consistently outperforms baselines across multiple tasks, ranging from graph-centric tasks (e.g., node classification, link prediction) to multimodal-centric generation tasks (e.g., graph2text, graph2image). The source code will be available upon acceptance.

