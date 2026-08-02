import { useMemo, useState } from "react";

const EMPTY_ROWS = [];

function SQLResult({ result }) {

    const [currentPage, setCurrentPage] = useState(1);
    const rowsPerPage = 8;

    const rows = result?.rows ?? EMPTY_ROWS;
    const columns = result?.columns ?? [];
    const totalPages = Math.max(1, Math.ceil(rows.length / rowsPerPage));

    const pagedRows = useMemo(() => {
        const startIndex = (currentPage - 1) * rowsPerPage;
        return rows.slice(startIndex, startIndex + rowsPerPage);
    }, [rows, currentPage]);

    if (!result) return null;

    return (

        <div className="result-panel">

            <div className="sql-preview-card">
                <h2>Generated SQL</h2>

                <pre>
                    {result.generated_sql}
                </pre>
            </div>

            <div className="result-table-card">
                <div className="result-table-header">
                    <h3>Rows Returned : {result.row_count}</h3>
                </div>

                <div className="table-wrapper">
                    <table>

                        <thead>

                        <tr>

                            {columns.map(col => (

                                <th key={col}>
                                    {col}
                                </th>

                            ))}

                        </tr>

                        </thead>

                        <tbody>

                        {pagedRows.map((row, index) => (

                            <tr key={`${row.join("-")}-${index}`}>

                                {row.map((cell, i) => (

                                    <td key={`${i}-${cell}`}>
                                        {String(cell)}
                                    </td>

                                ))}

                            </tr>

                        ))}

                        </tbody>

                    </table>
                </div>

                {totalPages > 1 && (
                    <div className="pagination">
                        <button
                            type="button"
                            className="pagination-btn"
                            onClick={() => setCurrentPage(prev => Math.max(1, prev - 1))}
                            disabled={currentPage === 1}
                        >
                            Previous
                        </button>

                        <span>Page {currentPage} of {totalPages}</span>

                        <button
                            type="button"
                            className="pagination-btn"
                            onClick={() => setCurrentPage(prev => Math.min(totalPages, prev + 1))}
                            disabled={currentPage === totalPages}
                        >
                            Next
                        </button>
                    </div>
                )}
            </div>

        </div>

    );
}

export default SQLResult;