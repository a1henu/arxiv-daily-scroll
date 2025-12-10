---
layout: default
title: Democratizing ML for Enterprise Security: A Self-Sustained Attack Detection Framework
---

# Democratizing ML for Enterprise Security: A Self-Sustained Attack Detection Framework
**arXiv**：[2512.08802v1](https://arxiv.org/abs/2512.08802) · [PDF](https://arxiv.org/pdf/2512.08802.pdf)  
**作者**：Sadegh Momeni, Ge Zhang, Birkett Huber, Hamza Harkous, Sam Lipton, Benoit Seguin, Yanis Pavlidis  

**一句话要点**：提出两阶段混合框架以降低企业安全中基于机器学习的攻击检测门槛

**关键词**：企业安全检测, 混合框架, 合成数据生成, 主动学习, YARA规则, ML分类器

## 3 点简述
- 核心问题：规则检测僵化导致高误报/漏报，ML方案资源密集且技能门槛高
- 方法要点：先松YARA规则粗筛，后ML分类器精筛，结合Simula生成合成数据克服数据稀缺
- 实验或效果：生产环境长期测试，日处理2500亿事件，通过主动学习持续提升模型精度

## 摘要（原文）

> Despite advancements in machine learning for security, rule-based detection remains prevalent in Security Operations Centers due to the resource intensiveness and skill gap associated with ML solutions. While traditional rule-based methods offer efficiency, their rigidity leads to high false positives or negatives and requires continuous manual maintenance. This paper proposes a novel, two-stage hybrid framework to democratize ML-based threat detection. The first stage employs intentionally loose YARA rules for coarse-grained filtering, optimized for high recall. The second stage utilizes an ML classifier to filter out false positives from the first stage's output. To overcome data scarcity, the system leverages Simula, a seedless synthetic data generation framework, enabling security analysts to create high-quality training datasets without extensive data science expertise or pre-labeled examples. A continuous feedback loop incorporates real-time investigation results to adaptively tune the ML model, preventing rule degradation.
>   This proposed model with active learning has been rigorously tested for a prolonged time in a production environment spanning tens of thousands of systems. The system handles initial raw log volumes often reaching 250 billion events per day, significantly reducing them through filtering and ML inference to a handful of daily tickets for human investigation. Live experiments over an extended timeline demonstrate a general improvement in the model's precision over time due to the active learning feature. This approach offers a self-sustained, low-overhead, and low-maintenance solution, allowing security professionals to guide model learning as expert ``teachers''.

