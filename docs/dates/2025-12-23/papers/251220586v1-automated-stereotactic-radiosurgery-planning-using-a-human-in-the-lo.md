---
layout: default
title: Automated stereotactic radiosurgery planning using a human-in-the-loop reasoning large language model agent
---

# Automated stereotactic radiosurgery planning using a human-in-the-loop reasoning large language model agent
**arXiv**：[2512.20586v1](https://arxiv.org/abs/2512.20586) · [PDF](https://arxiv.org/pdf/2512.20586.pdf)  
**作者**：Humza Nusrat, Luke Francisco, Bing Luo, Hassan Bagher-Ebadian, Joshua Kim, Karen Chin-Snyder, Salim Siddiqui, Mira Shah, Eric Mellon, Mohammad Ghassemi, Anthony Doemer, Benjamin Movsas, Kundan Thind  

**一句话要点**：提出基于推理大语言模型代理的自动化立体定向放射外科规划，以提升临床透明度和计划质量。

**关键词**：立体定向放射外科, 大语言模型代理, 自动化规划, 推理模型, 临床透明度, 剂量优化

## 3 点简述
- 核心问题：黑盒AI系统在立体定向放射外科规划中因不透明性而临床采纳受限。
- 方法要点：开发SAGE代理，比较推理与非推理模型在自动化规划中的表现。
- 实验或效果：推理模型在主要终点上与人工规划相当，并降低耳蜗剂量，同时提供可审计的优化痕迹。

## 摘要（原文）

> Stereotactic radiosurgery (SRS) demands precise dose shaping around critical structures, yet black-box AI systems have limited clinical adoption due to opacity concerns. We tested whether chain-of-thought reasoning improves agentic planning in a retrospective cohort of 41 patients with brain metastases treated with 18 Gy single-fraction SRS. We developed SAGE (Secure Agent for Generative Dose Expertise), an LLM-based planning agent for automated SRS treatment planning. Two variants generated plans for each case: one using a non-reasoning model, one using a reasoning model. The reasoning variant showed comparable plan dosimetry relative to human planners on primary endpoints (PTV coverage, maximum dose, conformity index, gradient index; all p > 0.21) while reducing cochlear dose below human baselines (p = 0.022). When prompted to improve conformity, the reasoning model demonstrated systematic planning behaviors including prospective constraint verification (457 instances) and trade-off deliberation (609 instances), while the standard model exhibited none of these deliberative processes (0 and 7 instances, respectively). Content analysis revealed that constraint verification and causal explanation concentrated in the reasoning agent. The optimization traces serve as auditable logs, offering a path toward transparent automated planning.

