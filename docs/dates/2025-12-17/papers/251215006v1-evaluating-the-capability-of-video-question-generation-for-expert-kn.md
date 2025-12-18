---
layout: default
title: Evaluating the Capability of Video Question Generation for Expert Knowledge Elicitation
---

# Evaluating the Capability of Video Question Generation for Expert Knowledge Elicitation
**arXiv**：[2512.15006v1](https://arxiv.org/abs/2512.15006) · [PDF](https://arxiv.org/pdf/2512.15006.pdf)  
**作者**：Huaying Zhang, Atsushi Hashimoto, Tosho Hirasawa  

**一句话要点**：提出基于检索的协议评估视频问题生成模型在专家知识获取中的能力

**关键词**：视频问题生成, 专家知识获取, 问答检索评估, EgoExoAsk数据集, 视频问答

## 3 点简述
- 核心问题：如何量化评估视频问题生成模型在从专家获取未知知识时的提问质量
- 方法要点：构建EgoExoAsk数据集，通过问题到答案检索模拟专家问答通信以评估模型
- 实验或效果：实验显示指标与模型访问更丰富上下文时表现更好一致，验证协议有效性

## 摘要（原文）

> Skilled human interviewers can extract valuable information from experts. This raises a fundamental question: what makes some questions more effective than others? To address this, a quantitative evaluation of question-generation models is essential. Video question generation (VQG) is a topic for video question answering (VideoQA), where questions are generated for given answers. Their evaluation typically focuses on the ability to answer questions, rather than the quality of generated questions. In contrast, we focus on the question quality in eliciting unseen knowledge from human experts. For a continuous improvement of VQG models, we propose a protocol that evaluates the ability by simulating question-answering communication with experts using a question-to-answer retrieval. We obtain the retriever by constructing a novel dataset, EgoExoAsk, which comprises 27,666 QA pairs generated from Ego-Exo4D's expert commentary annotation. The EgoExoAsk training set is used to obtain the retriever, and the benchmark is constructed on the validation set with Ego-Exo4D video segments. Experimental results demonstrate our metric reasonably aligns with question generation settings: models accessing richer context are evaluated better, supporting that our protocol works as intended. The EgoExoAsk dataset is available in https://github.com/omron-sinicx/VQG4ExpertKnowledge .

