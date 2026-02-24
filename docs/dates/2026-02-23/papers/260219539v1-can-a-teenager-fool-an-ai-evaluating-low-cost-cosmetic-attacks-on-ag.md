---
layout: default
title: Can a Teenager Fool an AI? Evaluating Low-Cost Cosmetic Attacks on Age Estimation Systems
---

# Can a Teenager Fool an AI? Evaluating Low-Cost Cosmetic Attacks on Age Estimation Systems
**arXiv**：[2602.19539v1](https://arxiv.org/abs/2602.19539) · [PDF](https://arxiv.org/pdf/2602.19539.pdf)  
**作者**：Xingyu Shen, Tommy Duong, Xiaodong An, Zengqi Zhao, Zebang Hu, Haoyu Hu, Ziyou Wang, Finn Guo, Simiao Ren  

**一句话要点**：评估低成本化妆攻击对年龄估计系统的影响，揭示其脆弱性

**关键词**：年龄估计系统, 化妆攻击, 对抗鲁棒性, 视觉语言模型, 攻击转换率

## 3 点简述
- 核心问题：年龄估计系统对化妆修改的鲁棒性未系统评估，可能被简单化妆攻击欺骗。
- 方法要点：使用VLM图像编辑器模拟胡须、白发等化妆攻击，在329张面部图像上测试八种模型。
- 实验效果：单一胡须攻击ACR达28-69%，组合攻击平均年龄增加7.7年，最高ACR达83%。

## 摘要（原文）

> Age estimation systems are increasingly deployed as gatekeepers for age-restricted online content, yet their robustness to cosmetic modifications has not been systematically evaluated. We investigate whether simple, household-accessible cosmetic changes, including beards, grey hair, makeup, and simulated wrinkles, can cause AI age estimators to classify minors as adults. To study this threat at scale without ethical concerns, we simulate these physical attacks on 329 facial images of individuals aged 10 to 21 using a VLM image editor (Gemini 2.5 Flash Image). We then evaluate eight models from our prior benchmark: five specialized architectures (MiVOLO, Custom-Best, Herosan, MiViaLab, DEX) and three vision-language models (Gemini 3 Flash, Gemini 2.5 Flash, GPT-5-Nano). We introduce the Attack Conversion Rate (ACR), defined as the fraction of images predicted as minor at baseline that flip to adult after attack, a population-agnostic metric that does not depend on the ratio of minors to adults in the test set. Our results reveal that a synthetic beard alone achieves 28 to 69 percent ACR across all eight models; combining all four attacks shifts predicted age by +7.7 years on average across all 329 subjects and reaches up to 83 percent ACR; and vision-language models exhibit lower ACR (59 to 71 percent) than specialized models (63 to 83 percent) under the full attack, although the ACR ranges overlap and the difference is not statistically tested. These findings highlight a critical vulnerability in deployed age-verification pipelines and call for adversarial robustness evaluation as a mandatory criterion for model selection.

