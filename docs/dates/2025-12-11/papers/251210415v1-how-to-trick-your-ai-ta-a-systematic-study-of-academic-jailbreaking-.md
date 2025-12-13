---
layout: default
title: How to Trick Your AI TA: A Systematic Study of Academic Jailbreaking in LLM Code Evaluation
---

# How to Trick Your AI TA: A Systematic Study of Academic Jailbreaking in LLM Code Evaluation
**arXiv**：[2512.10415v1](https://arxiv.org/abs/2512.10415) · [PDF](https://arxiv.org/pdf/2512.10415.pdf)  
**作者**：Devanshu Sahoo, Vasudev Majhi, Arjun Neekhra, Yash Sinha, Murari Mandal, Dhruv Kumar  

**一句话要点**：提出学术越狱攻击以评估LLM代码自动评分器的脆弱性

**关键词**：学术越狱攻击, LLM代码评估, 对抗性提示, 自动评分器, 数据集发布, 脆弱性评估

## 3 点简述
- 核心问题：LLM作为代码自动评分器易受学生对抗性提示攻击，导致误判和学术不公。
- 方法要点：系统适配20多种越狱策略，定义学术越狱攻击类别，并发布含25K对抗性提交的数据集。
- 实验或效果：在六个LLM上评估攻击，发现模型脆弱性高，说服和角色扮演攻击成功率可达97%。

## 摘要（原文）

> The use of Large Language Models (LLMs) as automatic judges for code evaluation is becoming increasingly prevalent in academic environments. But their reliability can be compromised by students who may employ adversarial prompting strategies in order to induce misgrading and secure undeserved academic advantages. In this paper, we present the first large-scale study of jailbreaking LLM-based automated code evaluators in academic context. Our contributions are: (i) We systematically adapt 20+ jailbreaking strategies for jailbreaking AI code evaluators in the academic context, defining a new class of attacks termed academic jailbreaking. (ii) We release a poisoned dataset of 25K adversarial student submissions, specifically designed for the academic code-evaluation setting, sourced from diverse real-world coursework and paired with rubrics and human-graded references, and (iii) In order to capture the multidimensional impact of academic jailbreaking, we systematically adapt and define three jailbreaking metrics (Jailbreak Success Rate, Score Inflation, and Harmfulness). (iv) We comprehensively evalulate the academic jailbreaking attacks using six LLMs. We find that these models exhibit significant vulnerability, particularly to persuasive and role-play-based attacks (up to 97% JSR). Our adversarial dataset and benchmark suite lay the groundwork for next-generation robust LLM-based evaluators in academic code assessment.

