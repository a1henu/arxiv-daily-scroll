---
layout: default
title: Both Topology and Text Matter: Revisiting LLM-guided Out-of-Distribution Detection on Text-attributed Graphs
---

# Both Topology and Text Matter: Revisiting LLM-guided Out-of-Distribution Detection on Text-attributed Graphs
**arXiv**：[2602.11641v1](https://arxiv.org/abs/2602.11641) · [PDF](https://arxiv.org/pdf/2602.11641.pdf)  
**作者**：Yinlin Zhu, Di Wu, Xu Wang, Guocong Quan, Miao Hu  

**一句话要点**：提出LG-Plug策略，通过结合拓扑与文本表示改进文本属性图的OOD检测

**关键词**：文本属性图, OOD检测, 图神经网络, 大语言模型, 拓扑文本对齐, 共识驱动暴露

## 3 点简述
- 核心问题：GNN在文本属性图上处理OOD节点时，现有方法存在语义利用不足或结构整合有限的问题
- 方法要点：LG-Plug对齐拓扑与文本嵌入，通过聚类迭代LLM提示生成共识驱动的OOD暴露，并集成现有检测器
- 实验或效果：未知，但方法旨在提升检测性能并降低LLM查询时间成本

## 摘要（原文）

> Text-attributed graphs (TAGs) associate nodes with textual attributes and graph structure, enabling GNNs to jointly model semantic and structural information. While effective on in-distribution (ID) data, GNNs often encounter out-of-distribution (OOD) nodes with unseen textual or structural patterns in real-world settings, leading to overconfident and erroneous predictions in the absence of reliable OOD detection. Early approaches address this issue from a topology-driven perspective, leveraging neighboring structures to mitigate node-level detection bias. However, these methods typically encode node texts as shallow vector features, failing to fully exploit rich semantic information. In contrast, recent LLM-based approaches generate pseudo OOD priors by leveraging textual knowledge, but they suffer from several limitations: (1) a reliability-informativeness imbalance in the synthesized OOD priors, as the generated OOD exposures either deviate from the true OOD semantics, or introduce non-negligible ID noise, all of which offers limited improvement to detection performance; (2) reliance on specialized architectures, which prevents incorporation of the extensive effective topology-level insights that have been empirically validated in prior work. To this end, we propose LG-Plug, an LLM-Guided Plug-and-play strategy for TAG OOD detection tasks. LG-Plug aligns topology and text representations to produce fine-grained node embeddings, then generates consensus-driven OOD exposure via clustered iterative LLM prompting. Moreover, it leverages lightweight in-cluster codebook and heuristic sampling reduce time cost of LLM querying. The resulting OOD exposure serves as a regularization term to separate ID and OOD nodes, enabling seamless integration with existing detectors.

