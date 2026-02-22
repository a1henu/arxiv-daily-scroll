---
layout: default
title: WarpRec: Unifying Academic Rigor and Industrial Scale for Responsible, Reproducible, and Efficient Recommendation
---

# WarpRec: Unifying Academic Rigor and Industrial Scale for Responsible, Reproducible, and Efficient Recommendation
**arXiv**：[2602.17442v1](https://arxiv.org/abs/2602.17442) · [PDF](https://arxiv.org/pdf/2602.17442.pdf)  
**作者**：Marco Avolio, Potito Aghilar, Sabino Roccotelli, Vito Walter Anelli, Chiara Mallamaci, Vincenzo Paparella, Marco Valentini, Alejandro Bellogín, Michelantonio Trizio, Joseph Trotta, Antonio Ferrara, Tommaso Di Noia  

**一句话要点**：提出WarpRec框架以统一学术实验与工业规模，支持负责任、可复现和高效的推荐系统开发

**关键词**：推荐系统框架, 分布式训练, 可持续计算, 可复现研究, 算法集成

## 3 点简述
- 核心问题：推荐系统生态分裂，学术实验与工业部署间存在效率与复杂性鸿沟
- 方法要点：采用后端无关架构，集成50+算法、40指标和19策略，支持本地到分布式无缝过渡
- 实验或效果：集成CodeCarbon实现实时能耗追踪，强调可扩展性与可持续性，代码已开源

## 摘要（原文）

> Innovation in Recommender Systems is currently impeded by a fractured ecosystem, where researchers must choose between the ease of in-memory experimentation and the costly, complex rewriting required for distributed industrial engines. To bridge this gap, we present WarpRec, a high-performance framework that eliminates this trade-off through a novel, backend-agnostic architecture. It includes 50+ state-of-the-art algorithms, 40 metrics, and 19 filtering and splitting strategies that seamlessly transition from local execution to distributed training and optimization. The framework enforces ecological responsibility by integrating CodeCarbon for real-time energy tracking, showing that scalability need not come at the cost of scientific integrity or sustainability. Furthermore, WarpRec anticipates the shift toward Agentic AI, leading Recommender Systems to evolve from static ranking engines into interactive tools within the Generative AI ecosystem. In summary, WarpRec not only bridges the gap between academia and industry but also can serve as the architectural backbone for the next generation of sustainable, agent-ready Recommender Systems. Code is available at https://github.com/sisinflab/warprec/

