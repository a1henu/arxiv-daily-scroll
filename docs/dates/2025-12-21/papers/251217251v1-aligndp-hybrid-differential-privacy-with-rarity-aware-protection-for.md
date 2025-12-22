---
layout: default
title: AlignDP: Hybrid Differential Privacy with Rarity-Aware Protection for LLMs
---

# AlignDP: Hybrid Differential Privacy with Rarity-Aware Protection for LLMs
**arXiv**：[2512.17251v1](https://arxiv.org/abs/2512.17251) · [PDF](https://arxiv.org/pdf/2512.17251.pdf)  
**作者**：Madhava Gaikwad  

**一句话要点**：提出AlignDP混合差分隐私方法，以保护大语言模型免受知识提取和未授权微调风险。

**关键词**：大语言模型隐私保护, 混合差分隐私, PAC不可区分性, RAPPOR, 知识提取防御, 本地差分隐私

## 3 点简述
- 核心问题：大语言模型面临知识提取、蒸馏和未授权微调风险，现有防御措施如水印或监控在泄露后生效。
- 方法要点：设计混合隐私锁，分离稀有和非稀有字段，稀有字段使用PAC不可区分性保护，非稀有字段使用RAPPOR进行本地差分隐私处理。
- 实验或效果：通过玩具模拟验证可行性，稀有类别保持隐藏，频繁类别以小误差恢复，分析效用权衡和隐私界限。

## 摘要（原文）

> Large language models are exposed to risks of extraction, distillation, and unauthorized fine-tuning. Existing defenses use watermarking or monitoring, but these act after leakage. We design AlignDP, a hybrid privacy lock that blocks knowledge transfer at the data interface. The key idea is to separate rare and non-rare fields. Rare fields are shielded by PAC indistinguishability, giving effective zero-epsilon local DP. Non-rare fields are privatized with RAPPOR, giving unbiased frequency estimates under local DP. A global aggregator enforces composition and budget. This two-tier design hides rare events and adds controlled noise to frequent events. We prove limits of PAC extension to global aggregation, give bounds for RAPPOR estimates, and analyze utility trade-off. A toy simulation confirms feasibility: rare categories remain hidden, frequent categories are recovered with small error.

