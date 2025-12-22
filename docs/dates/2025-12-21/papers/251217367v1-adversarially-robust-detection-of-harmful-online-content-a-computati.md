---
layout: default
title: Adversarially Robust Detection of Harmful Online Content: A Computational Design Science Approach
---

# Adversarially Robust Detection of Harmful Online Content: A Computational Design Science Approach
**arXiv**：[2512.17367v1](https://arxiv.org/abs/2512.17367) · [PDF](https://arxiv.org/pdf/2512.17367.pdf)  
**作者**：Yidong Chai, Yi Liu, Mohammadreza Ebrahimi, Weifeng Li, Balaji Padmanabhan  

**一句话要点**：提出LLM-SGA框架与ARHOCD检测器以增强有害在线内容检测的对抗鲁棒性

**关键词**：对抗鲁棒性, 有害内容检测, 大语言模型, 集成学习, 动态权重分配, 对抗训练

## 3 点简述
- 核心问题：社交媒体有害内容检测模型易受对抗攻击，需同时提升泛化性与准确性。
- 方法要点：基于LLM-SGA框架识别攻击不变性，ARHOCD集成多检测器、动态权重分配与对抗训练。
- 实验或效果：在仇恨言论、谣言和极端主义内容数据集上验证，ARHOCD在对抗条件下提升检测准确性与泛化性。

## 摘要（原文）

> Social media platforms are plagued by harmful content such as hate speech, misinformation, and extremist rhetoric. Machine learning (ML) models are widely adopted to detect such content; however, they remain highly vulnerable to adversarial attacks, wherein malicious users subtly modify text to evade detection. Enhancing adversarial robustness is therefore essential, requiring detectors that can defend against diverse attacks (generalizability) while maintaining high overall accuracy. However, simultaneously achieving both optimal generalizability and accuracy is challenging. Following the computational design science paradigm, this study takes a sequential approach that first proposes a novel framework (Large Language Model-based Sample Generation and Aggregation, LLM-SGA) by identifying the key invariances of textual adversarial attacks and leveraging them to ensure that a detector instantiated within the framework has strong generalizability. Second, we instantiate our detector (Adversarially Robust Harmful Online Content Detector, ARHOCD) with three novel design components to improve detection accuracy: (1) an ensemble of multiple base detectors that exploits their complementary strengths; (2) a novel weight assignment method that dynamically adjusts weights based on each sample's predictability and each base detector's capability, with weights initialized using domain knowledge and updated via Bayesian inference; and (3) a novel adversarial training strategy that iteratively optimizes both the base detectors and the weight assignor. We addressed several limitations of existing adversarial robustness enhancement research and empirically evaluated ARHOCD across three datasets spanning hate speech, rumor, and extremist content. Results show that ARHOCD offers strong generalizability and improves detection accuracy under adversarial conditions.

