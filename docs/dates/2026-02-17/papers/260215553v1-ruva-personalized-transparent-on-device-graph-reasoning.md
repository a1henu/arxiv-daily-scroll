---
layout: default
title: RUVA: Personalized Transparent On-Device Graph Reasoning
---

# RUVA: Personalized Transparent On-Device Graph Reasoning
**arXiv**：[2602.15553v1](https://arxiv.org/abs/2602.15553) · [PDF](https://arxiv.org/pdf/2602.15553.pdf)  
**作者**：Gabriele Conte, Alessio Mattiace, Gianni Carmosino, Potito Aghilar, Giovanni Servedio, Francesco Musicco, Vito Walter Anelli, Tommaso Di Noia, Francesco Maria Donini  

**一句话要点**：提出RUVA以解决个人AI中黑盒检索增强生成缺乏可问责性和隐私保护的问题

**关键词**：个人知识图谱, 图推理, 可解释AI, 隐私保护, 检索增强生成

## 3 点简述
- 核心问题：当前个人AI依赖黑盒检索增强生成，缺乏可解释性，无法精确删除敏感数据，违反隐私权。
- 方法要点：RUVA采用玻璃盒架构，基于个人知识图谱进行图推理，支持用户检查和精确编辑AI记忆。
- 实验或效果：未知，但项目提供演示视频，强调确保被遗忘权，用户可自主管理个人数据。

## 摘要（原文）

> The Personal AI landscape is currently dominated by "Black Box" Retrieval-Augmented Generation. While standard vector databases offer statistical matching, they suffer from a fundamental lack of accountability: when an AI hallucinates or retrieves sensitive data, the user cannot inspect the cause nor correct the error. Worse, "deleting" a concept from a vector space is mathematically imprecise, leaving behind probabilistic "ghosts" that violate true privacy. We propose Ruva, the first "Glass Box" architecture designed for Human-in-the-Loop Memory Curation. Ruva grounds Personal AI in a Personal Knowledge Graph, enabling users to inspect what the AI knows and to perform precise redaction of specific facts. By shifting the paradigm from Vector Matching to Graph Reasoning, Ruva ensures the "Right to be Forgotten." Users are the editors of their own lives; Ruva hands them the pen. The project and the demo video are available at http://sisinf00.poliba.it/ruva/.

