---
layout: default
title: Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks
---

# Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks
**arXiv**：[2601.04603v1](https://arxiv.org/abs/2601.04603) · [PDF](https://arxiv.org/pdf/2601.04603.pdf)  
**作者**：Hoagy Cunningham, Jerry Wei, Zihan Wang, Andrew Persic, Alwin Peng, Jordan Abderrachid, Raj Agarwal, Bobby Chen, Austin Cohen, Andy Dau, Alek Dimitriev, Rob Gilson, Logan Howard, Yijin Hua, Jared Kaplan, Jan Leike, Mu Lin, Christopher Liu, Vladimir Mikulik, Rohit Mittapalli, Clare O'Hara, Jin Pan, Nikhil Saxena, Alex Silverstein, Yue Song, Xunjie Yu, Giulio Zhou, Ethan Perez, Mrinank Sharma  

**一句话要点**：提出增强型宪法分类器，以高效生产级防御对抗通用越狱攻击

**关键词**：越狱攻击防御, 宪法分类器, 对话上下文评估, 分类器级联, 线性探针, 生产级安全

## 3 点简述
- 核心问题：现有防御系统计算成本高且易受孤立输出评估漏洞影响，需提升越狱攻击的鲁棒性。
- 方法要点：结合交换分类器评估完整对话上下文，采用两阶段级联分类器筛选，并集成线性探针与外部分类器以优化效率。
- 实验或效果：实现计算成本降低40倍，生产流量拒绝率0.05%，并通过1700多小时红队测试证明对通用越狱攻击的有效防护。

## 摘要（原文）

> We introduce enhanced Constitutional Classifiers that deliver production-grade jailbreak robustness with dramatically reduced computational costs and refusal rates compared to previous-generation defenses. Our system combines several key insights. First, we develop exchange classifiers that evaluate model responses in their full conversational context, which addresses vulnerabilities in last-generation systems that examine outputs in isolation. Second, we implement a two-stage classifier cascade where lightweight classifiers screen all traffic and escalate only suspicious exchanges to more expensive classifiers. Third, we train efficient linear probe classifiers and ensemble them with external classifiers to simultaneously improve robustness and reduce computational costs. Together, these techniques yield a production-grade system achieving a 40x computational cost reduction compared to our baseline exchange classifier, while maintaining a 0.05% refusal rate on production traffic. Through extensive red-teaming comprising over 1,700 hours, we demonstrate strong protection against universal jailbreaks -- no attack on this system successfully elicited responses to all eight target queries comparable in detail to an undefended model. Our work establishes Constitutional Classifiers as practical and efficient safeguards for large language models.

