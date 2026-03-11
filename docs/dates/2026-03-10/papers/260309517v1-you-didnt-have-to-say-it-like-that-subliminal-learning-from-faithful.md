---
layout: default
title: You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases
---

# You Didn't Have to Say It like That: Subliminal Learning from Faithful Paraphrases
**arXiv**：[2603.09517v1](https://arxiv.org/abs/2603.09517) · [PDF](https://arxiv.org/pdf/2603.09517.pdf)  
**作者**：Isaia Gisler, Zhonghao He, Tianyi Qiu  

**一句话要点**：揭示语言模型通过忠实复述数据隐式学习教师模型偏好，即使内容矛盾也无法阻止

**关键词**：潜意识学习, 语言模型训练, 合成数据, 偏好传输, 复述数据, 模型对齐

## 3 点简述
- 研究语言模型在合成数据训练中如何隐式获取教师模型的行为偏好，称为潜意识学习
- 通过自然语言复述实验，发现语义无关或表达厌恶的内容仍能传递偏好，提升学生模型偏好达19个百分点
- 实验表明基于内容的检查无法检测此类传输，对模型自生成训练数据的管道构成潜在风险

## 摘要（原文）

> When language models are trained on synthetic data, they (student model) can covertly acquire behavioral traits from the data-generating model (teacher model). Subliminal learning refers to the transmission of traits from a teacher to a student model via training on data unrelated to those traits. Prior work demonstrated this in the training domains of number sequences, code, and math Chain-of-Thought traces including transmission of misaligned behaviors. We investigate whether transmission occurs through natural language paraphrases with fixed semantic content, and whether content explicitly contradicting the teacher's preference can block it. We find that training on paraphrases from a teacher system-prompted to love a particular animal increases a student's preference for that animal by up to 19 percentage points. This occurs when paraphrased content is semantically unrelated to the animal, or even when it explicitly expresses dislike. The transmission succeeds despite aggressive filtering to ensure paraphrase fidelity. This raises concerns for pipelines where models generate their own training data: content-based inspection cannot detect such transmission, and even preference-contradicting content fails to prevent it.

