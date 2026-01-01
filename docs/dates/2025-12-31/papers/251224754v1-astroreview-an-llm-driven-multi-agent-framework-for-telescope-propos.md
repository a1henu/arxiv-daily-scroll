---
layout: default
title: AstroReview: An LLM-driven Multi-Agent Framework for Telescope Proposal Peer Review and Refinement
---

# AstroReview: An LLM-driven Multi-Agent Framework for Telescope Proposal Peer Review and Refinement
**arXiv**：[2512.24754v1](https://arxiv.org/abs/2512.24754) · [PDF](https://arxiv.org/pdf/2512.24754.pdf)  
**作者**：Yutong Wang, Yunxiang Xiao, Yonglin Tian, Junyong Li, Jing Wang, Yisheng Lv  

**一句话要点**：提出AstroReview框架，基于LLM多代理自动化望远镜提案评审与优化，以解决天文学提案评审的瓶颈问题。

**关键词**：多代理系统, 自动化评审, 望远镜提案, LLM驱动, 元评审, 可靠性验证

## 3 点简述
- 核心问题：望远镜时间竞争激烈，提案量远超可用资源，传统同行评审存在效率低、一致性差和透明度不足的瓶颈。
- 方法要点：采用开源多代理框架，分三阶段自动化评审：新颖性与科学价值、可行性与预期产出、元评审与可靠性验证，通过任务隔离和显式推理轨迹减少幻觉。
- 实验或效果：在实验中，仅用于最后阶段时正确识别接受提案的准确率达87%；结合迭代反馈，修订草案的接受率在两轮后提升66%。

## 摘要（原文）

> Competitive access to modern observatories has intensified as proposal volumes outpace available telescope time, making timely, consistent, and transparent peer review a critical bottleneck for the advancement of astronomy. Automating parts of this process is therefore both scientifically significant and operationally necessary to ensure fair allocation and reproducible decisions at scale. We present AstroReview, an open-source, agent-based framework that automates proposal review in three stages: (i) novelty and scientific merit, (ii) feasibility and expected yield, and (iii) meta-review and reliability verification. Task isolation and explicit reasoning traces curb hallucinations and improve transparency. Without any domain specific fine tuning, AstroReview used in our experiments only for the last stage, correctly identifies genuinely accepted proposals with an accuracy of 87%. The AstroReview in Action module replicates the review and refinement loop; with its integrated Proposal Authoring Agent, the acceptance rate of revised drafts increases by 66% after two iterations, showing that iterative feedback combined with automated meta-review and reliability verification delivers measurable quality gains. Together, these results point to a practical path toward scalable, auditable, and higher throughput proposal review for resource limited facilities.

