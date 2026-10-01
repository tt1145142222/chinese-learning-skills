# 毛概/毛中特大题复习文档输出规格

Use this reference when generating a chapter-based exam review document set from local course materials.

## Default document pair

Create two separate `.docx` files:

1. 题目练习版：用于背诵后练习，包含题目和留白。
2. 答案解析版：用于订正，包含题目、考点、参考答案、解析或评分提示。

## Opening section

The 题目练习版 should start with a short usage guide and a table-style复习计划. A strong default is:

- 15天逐章复习，最后1天总复盘；
- 每天流程：先看本章重点回顾，再闭卷做题，最后用答案版订正；
- 三星题优先背熟，两星题巩固，一星题用于查漏补缺。

## Chapter structure

Each chapter should use this order:

1. 章节标题
2. 本章知识复习和重点回顾
3. 辨析题
4. 简答题
5. 材料分析题

The chapter review should be concise and exam-facing. It does not need to cover every textbook detail; it should prepare the student for the questions that follow.

## Default question counts

Unless the user gives a different exam format:

- 辨析题：每章 2-4 题；default 2 题。
- 简答题：每章 4-8 题；default 4 题。
- 材料分析题：每章 1-2 题；default 1 题。

These defaults mirror the common exam baseline while keeping the document compact.

## Star levels

Use star markers on every question:

- `★★★`：高频核心考点，优先背熟。
- `★★`：重要但相对次一级，适合巩固。
- `★`：补充或低频考点，用于查漏。

Avoid making everything `★★★`; the star distribution should guide review priority.

## Question-writing standards

Good questions should:

- match the user-provided exam types;
- cover the chapter's central concepts, historical logic, theoretical contribution, and practical meaning;
- use precise political-theory wording without unnecessary expansion;
- avoid overlapping too heavily with another question in the same chapter;
- be answerable from the provided materials.

## Answer-writing standards

For each question in the answer document, include:

- `【题目】` or the full question line;
- `【考点定位】`：state the tested knowledge point;
- `【参考答案】`：give a concise but complete answer suitable for memorization;
- `【作答解析】`：explain why the answer is organized this way, common traps, or scoring emphasis.

For 辨析题, explicitly state whether the proposition is correct, wrong, or one-sided, then analyze.

For 材料分析题, preserve the material prompt in the answer document and answer each subquestion separately.

## Minimum QA checklist

Before delivery, verify:

- two documents exist and open as DOCX;
- no placeholder text remains;
- all chapters have all three question types;
- every chapter has a concise review section;
- answer version is not answer-only;
- question and answer numbering are aligned;
- formatting is readable and proportionate.
