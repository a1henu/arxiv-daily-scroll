---
layout: default
title: CME-CAD: Heterogeneous Collaborative Multi-Expert Reinforcement Learning for CAD Code Generation
---

# CME-CAD: Heterogeneous Collaborative Multi-Expert Reinforcement Learning for CAD Code Generation
**arXiv**：[2512.23333v1](https://arxiv.org/abs/2512.23333) · [PDF](https://arxiv.org/pdf/2512.23333.pdf)  
**作者**：Ke Niu, Haiyang Yu, Zhuofan Chen, Zhengtao Yao, Weitao Jia, Xiaodong Ge, Jingqun Tang, Benlei Cui, Bin Li, Xiangyang Xue  

**一句话要点**：提出异构协同多专家强化学习范式以解决CAD代码生成中精度与可编辑性不足的问题

**关键词**：CAD代码生成, 多专家强化学习, 异构协同学习, 工业设计自动化, 开源基准

## 3 点简述
- 现有方法从草图重建3D模型常产生不可编辑的近似模型，难以满足工业设计的高精度要求
- 提出CME-CAD范式，通过多专家微调和强化学习两阶段训练，整合互补优势生成精确、约束兼容的CAD模型
- 构建CADExpert开源基准，包含17299个实例，提供正交投影、专家思维链、可执行代码和渲染模型

## 摘要（原文）

> Computer-Aided Design (CAD) is essential in industrial design, but the complexity of traditional CAD modeling and workflows presents significant challenges for automating the generation of high-precision, editable CAD models. Existing methods that reconstruct 3D models from sketches often produce non-editable and approximate models that fall short of meeting the stringent requirements for precision and editability in industrial design. Moreover, the reliance on text or image-based inputs often requires significant manual annotation, limiting their scalability and applicability in industrial settings. To overcome these challenges, we propose the Heterogeneous Collaborative Multi-Expert Reinforcement Learning (CME-CAD) paradigm, a novel training paradigm for CAD code generation. Our approach integrates the complementary strengths of these models, facilitating collaborative learning and improving the model's ability to generate accurate, constraint-compatible, and fully editable CAD models. We introduce a two-stage training process: Multi-Expert Fine-Tuning (MEFT), and Multi-Expert Reinforcement Learning (MERL). Additionally, we present CADExpert, an open-source benchmark consisting of 17,299 instances, including orthographic projections with precise dimension annotations, expert-generated Chain-of-Thought (CoT) processes, executable CADQuery code, and rendered 3D models.

