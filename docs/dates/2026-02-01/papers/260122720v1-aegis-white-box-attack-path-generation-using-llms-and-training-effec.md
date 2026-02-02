---
layout: default
title: AEGIS: White-Box Attack Path Generation using LLMs and Training Effectiveness Evaluation for Large-Scale Cyber Defence Exercises
---

# AEGIS: White-Box Attack Path Generation using LLMs and Training Effectiveness Evaluation for Large-Scale Cyber Defence Exercises
**arXiv**：[2601.22720v1](https://arxiv.org/abs/2601.22720) · [PDF](https://arxiv.org/pdf/2601.22720.pdf)  
**作者**：Ivan K. Tung, Yu Xiang Shi, Alex Chien, Wenkai Liu, Lawrence Zheng  

**一句话要点**：提出AEGIS系统，利用LLM和白盒访问自动生成网络防御演练攻击路径，将场景开发从数月缩短至数天。

**关键词**：网络防御演练, 攻击路径生成, 大语言模型, 白盒访问, 蒙特卡洛树搜索, 自动化场景开发

## 3 点简述
- 核心问题：网络防御演练攻击路径创建依赖专家手动构建，现有自动化方法需预定义漏洞图或利用集，应用受限。
- 方法要点：结合LLM动态发现利用、白盒访问验证利用、蒙特卡洛树搜索执行真实利用，无需预定义漏洞图。
- 实验效果：在46台主机的CIDeX 2025演练中，AEGIS生成路径在训练体验四个维度上与人写场景相当，问卷验证可扩展至模拟训练。

## 摘要（原文）

> Creating attack paths for cyber defence exercises requires substantial expert effort. Existing automation requires vulnerability graphs or exploit sets curated in advance, limiting where it can be applied. We present AEGIS, a system that generates attack paths using LLMs, white-box access, and Monte Carlo Tree Search over real exploit execution. LLM-based search discovers exploits dynamically without pre-existing vulnerability graphs, while white-box access enables validating exploits in isolation before committing to attack paths. Evaluation at CIDeX 2025, a large-scale exercise spanning 46 IT hosts, showed that AEGIS-generated paths are comparable to human-authored scenarios across four dimensions of training experience (perceived learning, engagement, believability, challenge). Results were measured with a validated questionnaire extensible to general simulation-based training. By automating exploit chain discovery and validation, AEGIS reduces scenario development from months to days, shifting expert effort from technical validation to scenario design.

