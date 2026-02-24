---
layout: default
title: Learning Mutual View Information Graph for Adaptive Adversarial Collaborative Perception
---

# Learning Mutual View Information Graph for Adaptive Adversarial Collaborative Perception
**arXiv**：[2602.19596v1](https://arxiv.org/abs/2602.19596) · [PDF](https://arxiv.org/pdf/2602.19596.pdf)  
**作者**：Yihang Tao, Senkang Hu, Haonan An, Zhengru Fang, Hangcheng Cao, Yuguang Fang  

**一句话要点**：提出MVIG攻击框架，通过互视图信息图学习自适应对抗协同感知漏洞

**关键词**：协同感知, 对抗攻击, 图表示学习, 自适应攻击, 自动驾驶安全

## 3 点简述
- 协同感知系统易受特征级扰动攻击，现有防御缺乏对时序和区域优化攻击的鲁棒性
- MVIG攻击利用互视图信息图表示和时序图学习生成动态伪造风险图，结合熵感知漏洞搜索优化攻击参数
- 在OPV2V和Adv-OPV2V数据集上，MVIG攻击降低防御成功率高达62%，暴露CP系统安全漏洞

## 摘要（原文）

> Collaborative perception (CP) enables data sharing among connected and autonomous vehicles (CAVs) to enhance driving safety. However, CP systems are vulnerable to adversarial attacks where malicious agents forge false objects via feature-level perturbations. Current defensive systems use threshold-based consensus verification by comparing collaborative and ego detection results. Yet, these defenses remain vulnerable to more sophisticated attack strategies that could exploit two critical weaknesses: (i) lack of robustness against attacks with systematic timing and target region optimization, and (ii) inadvertent disclosure of vulnerability knowledge through implicit confidence information in shared collaboration data. In this paper, we propose MVIG attack, a novel adaptive adversarial CP framework learning to capture vulnerability knowledge disclosed by different defensive CP systems from a unified mutual view information graph (MVIG) representation. Our approach combines MVIG representation with temporal graph learning to generate evolving fabrication risk maps and employs entropy-aware vulnerability search to optimize attack location, timing and persistence, enabling adaptive attacks with generalizability across various defensive configurations. Extensive evaluations on OPV2V and Adv-OPV2V datasets demonstrate that MVIG attack reduces defense success rates by up to 62\% against state-of-the-art defenses while achieving 47\% lower detection for persistent attacks at 29.9 FPS, exposing critical security gaps in CP systems. Code will be released at https://github.com/yihangtao/MVIG.git

