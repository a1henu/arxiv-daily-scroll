---
layout: default
title: Teaching Language Models Mechanistic Explainability Through Arrow-Pushing
---

# Teaching Language Models Mechanistic Explainability Through Arrow-Pushing
**arXiv**：[2512.05722v1](https://arxiv.org/abs/2512.05722) · [PDF](https://arxiv.org/pdf/2512.05722.pdf)  
**作者**：Théo A. Neukomm, Zlatko Jončev, Philippe Schwaller  

**一句话要点**：提出基于箭头推演形式化教学语言模型预测化学反应机制，以提升计算机辅助合成规划的可解释性与化学有效性。

**关键词**：化学反应机制预测, 语言模型教学, 计算机辅助合成规划, 可解释人工智能, 电子流跟踪, 机制验证

## 3 点简述
- 当前计算机辅助合成规划系统缺乏机制基础，导致预测缺乏可解释性。
- 开发MechSMILES文本格式编码分子结构与电子流，训练语言模型完成从基础步骤到完整机制的预测任务。
- 模型在基础步骤预测中达到95%以上top-3准确率，在完整机制检索任务中在mech-USPTO-31k和FlowER数据集上分别超过73%和93%。

## 摘要（原文）

> Chemical reaction mechanisms provide crucial insight into synthesizability, yet current Computer-Assisted Synthesis Planning (CASP) systems lack mechanistic grounding. We introduce a computational framework for teaching language models to predict chemical reaction mechanisms through arrow pushing formalism, a century-old notation that tracks electron flow while respecting conservation laws. We developed MechSMILES, a compact textual format encoding molecular structure and electron flow, and trained language models on four mechanism prediction tasks of increasing complexity using mechanistic reaction datasets, such as mech-USPTO-31k and FlowER. Our models achieve more than 95\% top-3 accuracy on elementary step prediction and scores that surpass 73\% on mech-USPTO-31k, and 93\% on FlowER dataset for the retrieval of complete reaction mechanisms on our hardest task. This mechanistic understanding enables three key applications. First, our models serve as post-hoc validators for CASP systems, filtering chemically implausible transformations. Second, they enable holistic atom-to-atom mapping that tracks all atoms, including hydrogens. Third, they extract catalyst-aware reaction templates that distinguish recycled catalysts from spectator species. By grounding predictions in physically meaningful electron moves that ensure conservation of mass and charge, this work provides a pathway toward more explainable and chemically valid computational synthesis planning, while providing an architecture-agnostic framework for the benchmarking of mechanism prediction.

